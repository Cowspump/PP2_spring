import random
import pygame
import os

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("inf road to KBTU DLC")

# Получаем путь к текущей директории
BASE_PATH = os.path.dirname(__file__)

# Загрузка фонового изображения
background = pygame.image.load(os.path.join(BASE_PATH, "assets_cars", "road_cars.png"))
bg_height = background.get_height()

# Переменные
FPS = 60
enemy_speed = 4  # Настраиваемая скорость врагов
COIN_IMAGE_PATH = os.path.join(BASE_PATH, "assets_cars", "coin_cars.png")
coins_img = pygame.image.load(COIN_IMAGE_PATH)

CAR_SPRITES = [
    os.path.join(BASE_PATH, "assets_cars", "car_skins", "car_27.png"),
    os.path.join(BASE_PATH, "assets_cars", "car_skins", "car_50.png"),
    os.path.join(BASE_PATH, "assets_cars", "car_skins", "car_51.png")
]

ENEMY_CAR_PATH = os.path.join(BASE_PATH, "assets_cars", "enemy_cars")
enemy_car_sprites = [os.path.join(ENEMY_CAR_PATH, f) for f in os.listdir(ENEMY_CAR_PATH) if f.endswith(".png")]

LANES = [WIDTH // 4 - 50, WIDTH // 2 - 50, 3 * WIDTH // 4 - 50, WIDTH - 150]


def choose_car():
    selected_car = 0
    running = True
    while running:
        screen.fill((50, 50, 50))
        font = pygame.font.Font(None, 36)
        text = font.render("Выберите машину (\u2190 \u2192), Enter для старта", True, (255, 255, 255))
        screen.blit(text, (WIDTH // 4, HEIGHT // 8))

        for i, car_path in enumerate(CAR_SPRITES):
            car_image = pygame.image.load(car_path)
            car_image = pygame.transform.scale(car_image, (50, 100))
            x = WIDTH // 2 + (i - 1) * 100
            y = HEIGHT // 2
            screen.blit(car_image, (x, y))
            if i == selected_car:
                pygame.draw.rect(screen, (255, 255, 0), (x, y, 50, 100), 3)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_car = (selected_car - 1) % len(CAR_SPRITES)
                if event.key == pygame.K_RIGHT:
                    selected_car = (selected_car + 1) % len(CAR_SPRITES)
                if event.key == pygame.K_RETURN:
                    running = False
    return CAR_SPRITES[selected_car]

class Coin:
    def __init__(self, existing_objects):
        self.image = pygame.transform.scale(coins_img, (30, 30))
        self.value = random.randint(1, 3)  # Монеты имеют разную ценность
        self.relocate(existing_objects)

    def relocate(self, existing_objects):
        max_attempts = 10
        for _ in range(max_attempts):
            self.rect = pygame.Rect(random.choice(LANES), random.randint(-500, -50), 30, 30)
            if not any(self.rect.colliderect(obj.rect) for obj in existing_objects):
                return

    def move(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.relocate([])

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Car:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class EnemyCar:
    def __init__(self, existing_objects, speed=4):
        self.speed = speed
        while True:
            self.rect = pygame.Rect(random.choice(LANES), random.randint(HEIGHT + 50, HEIGHT + 600), 50, 100)
            if not any(self.rect.colliderect(obj.rect) for obj in existing_objects):
                break
        self.image = pygame.image.load(random.choice(enemy_car_sprites))
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.image = pygame.transform.flip(self.image, False, True)  # Разворачиваем вверх

    def move(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.relocate()

    def relocate(self):
        self.rect.y = random.randint(HEIGHT + 50, HEIGHT + 600)
        self.rect.x = random.choice(LANES)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    global enemy_speed
    bg_y = 0
    speed = 5

    car_image = choose_car()
    if not car_image:
        return

    car = Car(WIDTH // 2, HEIGHT - 250, car_image)
    enemy_cars = [EnemyCar([], speed=enemy_speed) for _ in range(3)]
    coins_list = [Coin(enemy_cars) for _ in range(5)]
    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg_y = (bg_y + speed) % bg_height
        screen.blit(background, (0, bg_y - bg_height))
        screen.blit(background, (0, bg_y))

        keys = pygame.key.get_pressed()
        car.move(keys)
        car.draw(screen)

        if len(coins_list) < 5:
            coins_list.append(Coin(enemy_cars + coins_list))

        for coin in coins_list:
            coin.move()
            coin.draw(screen)
            if car.rect.colliderect(coin.rect):
                score += coin.value  # Учитываем разный вес монет
                coin.relocate(enemy_cars + coins_list)

        if score >= 10:
            enemy_speed = 6
        if score >= 20:
            enemy_speed = 7
        if score >= 50:
            enemy_speed = 9
        if score >= 65:
            enemy_speed = 12
        if score >= 80:
            enemy_speed = 16

        for enemy in enemy_cars:
            enemy.move()
            enemy.draw(screen)
            if car.rect.colliderect(enemy.rect):
                running = False

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH - 120, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
