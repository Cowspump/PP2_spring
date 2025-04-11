import random
import pygame as pg
from pygame import Vector2
import sys
import psycopg2 as psg

# DB Connection
conn = psg.connect(host='localhost', dbname="snakePoints", user="postgres", password="1234", port=5432)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(20) PRIMARY KEY,
    games_played INT NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS users_points(
    username VARCHAR(20) PRIMARY KEY,
    high_score INT NOT NULL
)""")
conn.commit()

# Screen settings
OFFSET = 80
cell_size = 40
cell_number = 20
pg.init()
screen = pg.display.set_mode((OFFSET*2+cell_size*cell_number, OFFSET*2+cell_size*cell_number))
pg.display.set_caption('Snake with Levels and Obstacles')

# Colors
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
RED = (200, 30, 30)
clock = pg.time.Clock()
title_font = pg.font.SysFont('Arial', 30)

def get_username():
    input_active = True
    user_text = ''
    input_box = pg.Rect(OFFSET, OFFSET, 300, 50)
    input_color = (255, 255, 255)
    text_color = (0, 0, 0)
    while input_active:
        screen.fill(GREEN)
        pg.draw.rect(screen, input_color, input_box, 0, 7)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    return user_text if user_text else "anonymous"
                elif event.key == pg.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if len(user_text) < 12:
                        user_text += event.unicode
        text_surface = title_font.render(f"Name: {user_text}", True, text_color)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        instructions = title_font.render("Enter your name and press ENTER", True, (0, 0, 0))
        screen.blit(instructions, (OFFSET, OFFSET - 50))
        pg.display.flip()
        clock.tick(30)

username = get_username()

# Insert user if not exists
cur.execute("SELECT * FROM users WHERE username=%s", (username,))
if not cur.fetchone():
    cur.execute("INSERT INTO users (username, games_played) VALUES (%s, %s)", (username, 0))
    cur.execute("INSERT INTO users_points (username, high_score) VALUES (%s, %s)", (username, 0))
    conn.commit()

class UserPoints:
    def __init__(self):
        self.points = 0
        self.high_score = self.load_high_score()

    def load_high_score(self):
        cur.execute("SELECT high_score FROM users_points WHERE username=%s", (username,))
        result = cur.fetchone()
        return result[0] if result else 0

    def reset_points(self):
        self.points = 0

    def add(self, point):
        self.points += point  # больше не обновляет high_score

    def save_if_high_score(self):
        if self.points > self.high_score:
            self.high_score = self.points
            cur.execute("UPDATE users_points SET high_score = %s WHERE username = %s", (self.high_score, username))
            conn.commit()
            return True
        return False

class Snake:
    def __init__(self, x, y):
        self.body = [Vector2(x, y)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def move(self):
        if self.new_block:
            self.body.insert(0, self.body[0] + self.direction)
            self.new_block = False
        else:
            self.body.insert(0, self.body[0] + self.direction)
            self.body.pop()

    def reset(self):
        self.body = [Vector2(1, 1)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw(self):
        for i, block in enumerate(self.body):
            rect = pg.Rect(OFFSET + block.x * cell_size, OFFSET + block.y * cell_size, cell_size, cell_size)
            color = (106, 190, 48) if i == 0 else DARK_GREEN
            pg.draw.rect(screen, color, rect, 0, 7)

class Food:
    def __init__(self, snake, blocks):
        self.pos = Vector2()
        self.snake = snake
        self.blocks = blocks
        self.random_pos()

    def random_pos(self):
        while True:
            new_pos = Vector2(random.randint(0, 19), random.randint(0, 19))
            if new_pos not in self.snake.body and new_pos not in self.blocks:
                self.pos = new_pos
                break

    def draw(self):
        rect = pg.Rect(OFFSET + self.pos.x * cell_size, OFFSET + self.pos.y * cell_size, cell_size, cell_size)
        pg.draw.rect(screen, RED, rect)

    def eat_food(self, snake):
        snake.new_block = True
        self.random_pos()

class MAIN:
    def __init__(self):
        self.snake = Snake(1, 1)
        self.level = 1
        self.blocks = []
        self.user_points = UserPoints()
        self.food = Food(self.snake, self.blocks)
        self.speed = level_speed[self.level]

    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_level_up()

    def draw_all(self):
        self.snake.draw()
        self.food.draw()
        for block in self.blocks:
            rect = pg.Rect(OFFSET + block.x * cell_size, OFFSET + block.y * cell_size, cell_size, cell_size)
            pg.draw.rect(screen, (70, 70, 70), rect)

    def end_game(self):
        self.user_points.save_if_high_score()
        self.snake.reset()
        self.user_points.reset_points()
        self.level = 1
        self.speed = level_speed[self.level]
        self.blocks = []
        self.food = Food(self.snake, self.blocks)
        pg.time.set_timer(GAME_UPDATE, self.speed)


    def check_collision(self):
        head = self.snake.body[0]
        if head.x < 0 or head.x >= cell_number or head.y < 0 or head.y >= cell_number:
            self.end_game()
        if head in self.snake.body[1:] or head in self.blocks:
            self.end_game()
        if head == self.food.pos:
            self.food.eat_food(self.snake)
            self.user_points.add(1)

    def check_level_up(self):
        if self.user_points.points == 10 and self.level == 1:
            self.level = 2
            self.speed = level_speed[2]
            self.blocks = [Vector2(5, 5), Vector2(6, 5), Vector2(7, 5)]
            self.food = Food(self.snake, self.blocks)
            pg.time.set_timer(GAME_UPDATE, self.speed)
        elif self.user_points.points == 20 and self.level == 2:
            self.level = 3
            self.speed = level_speed[3]
            self.blocks += [Vector2(10, 10), Vector2(10, 11), Vector2(10, 12), Vector2(2, 8), Vector2(3, 8)]
            self.food = Food(self.snake, self.blocks)
            pg.time.set_timer(GAME_UPDATE, self.speed)

# Speeds for levels
level_speed = {1: 150, 2: 100, 3: 80}

main_game = MAIN()
GAME_UPDATE = pg.USEREVENT
pg.time.set_timer(GAME_UPDATE, main_game.speed)
running = True

# Show leaderboard
print("\n🏆 Leaderboard:")
cur.execute("SELECT * FROM users_points ORDER BY high_score DESC LIMIT 5")
for i, row in enumerate(cur.fetchall(), 1):
    print(f"{i}) {row[0]} - {row[1]} pts")

# Game loop

paused = False
show_save_message = False
save_message_timer = 0

while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                paused = not paused
                if paused:
                    print("⏸ Game Paused")
                else:
                    print("▶️ Game Resumed")

            if paused:
                if event.key == pg.K_s:
                    if main_game.user_points.save_if_high_score():
                        print(f"✔️ Saved new high score: {main_game.user_points.high_score}")
                        show_save_message = True
                        save_message_timer = pg.time.get_ticks()
                    else:
                        print("ℹ️ Your current score is not higher than your saved high score.")
            else:
                if event.key == pg.K_RIGHT and main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
                elif event.key == pg.K_LEFT and main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                elif event.key == pg.K_UP and main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
                elif event.key == pg.K_DOWN and main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)

        if event.type == GAME_UPDATE and not paused:
            main_game.update()

    screen.fill(GREEN)
    score = title_font.render(f"Score: {main_game.user_points.points}", True, (0, 0, 0))
    high_score = title_font.render(f"High Score: {main_game.user_points.high_score}", True, (0, 0, 0))
    player = title_font.render(f"Player: {username}", True, (0, 0, 0))
    level = title_font.render(f"Level: {main_game.level}", True, (0, 0, 0))

    screen.blit(score, (OFFSET - 5, 20))
    screen.blit(high_score, (300, 20))
    screen.blit(player, (600, 20))
    screen.blit(level, (100, 800))

    if show_save_message and pg.time.get_ticks() - save_message_timer < 2000:
        save_msg = title_font.render("✔️ Saved!", True, (0, 100, 0))
        screen.blit(save_msg, (500, 800))
    elif pg.time.get_ticks() - save_message_timer >= 2000:
        show_save_message = False

    pg.draw.rect(screen, DARK_GREEN, (OFFSET - 5, OFFSET - 5, cell_size * cell_number + 10, cell_size * cell_number + 10), 5)
    main_game.draw_all()
    pg.display.update()
