import pygame as pg
import sys, random
from pygame import Vector2

# Pygame setup
pg.init()
clock = pg.time.Clock()

cell_size = 40
cell_number = 20

screen = pg.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pg.display.set_caption("Snake Game")

game_font = pg.font.Font('freesansbold.ttf', 25)

# Define different food types with their weights and lifetime
FOOD_TYPES = {
    "apple": {"color": (211, 25, 55), "points": 1, "lifetime": 5000},
    "banana": {"color": (255, 255, 0), "points": 2, "lifetime": 4000},
    "grape": {"color": (138, 43, 226), "points": 3, "lifetime": 3000}
}


class FRUIT:
    def __init__(self, snake):
        self.snake = snake
        self.spawn_fruit()

    def draw_fruit(self):
        fruit_rect = pg.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pg.draw.rect(screen, self.color, fruit_rect)

    def spawn_fruit(self):
        while True:
            self.pos = Vector2(random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))
            if self.pos not in self.snake.body:
                break

        self.type = random.choice(list(FOOD_TYPES.keys()))
        self.color = FOOD_TYPES[self.type]["color"]
        self.points = FOOD_TYPES[self.type]["points"]
        self.lifetime = FOOD_TYPES[self.type]["lifetime"]
        self.spawn_time = pg.time.get_ticks()  # Track when fruit is spawned

    def check_expiration(self):
        if pg.time.get_ticks() - self.spawn_time > self.lifetime:
            self.spawn_fruit()


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            body_block = pg.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pg.draw.rect(screen, (64, 109, 228), body_block)

    def move_snake(self):
        if self.new_block:
            self.body.insert(0, self.body[0] + self.direction)
            self.new_block = False
        else:
            self.body.pop()
            self.body.insert(0, self.body[0] + self.direction)

    def add_block(self):
        self.new_block = True


class MAIN:
    def __init__(self):
        self.snake = Snake()
        self.fruit = FRUIT(self.snake)
        self.score = 0
        self.level = 1
        self.speed = 150

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.fruit.check_expiration()

    def draw(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_text()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.score += self.fruit.points  # Increase score by fruit points
            self.snake.add_block()
            self.fruit.spawn_fruit()

            if self.score % 5 == 0:
                self.level_up()

    def level_up(self):
        if self.level < 5:
            self.level += 1
            self.speed = max(50, self.speed - 20)
            pg.time.set_timer(SCREEN_UPDATE, self.speed)

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pg.quit()
        sys.exit()

    def draw_text(self):
        score_text = f"Score: {self.score}"
        level_text = f"Level: {self.level}"
        screen.blit(game_font.render(score_text, True, (255, 255, 255)), (10, 10))
        screen.blit(game_font.render(level_text, True, (255, 255, 255)), (10, 40))


SCREEN_UPDATE = pg.USEREVENT
main_game = MAIN()
pg.time.set_timer(SCREEN_UPDATE, main_game.speed)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pg.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pg.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pg.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)

    screen.fill((170, 215, 81))
    main_game.draw()
    pg.display.flip()
    clock.tick(60)