import pygame
import math

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Tool")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_color = BLACK

# Переменные
clock = pygame.time.Clock()
running = True
drawing = False
mode = "brush"  # brush, eraser, rect, circle, square, right_triangle, equilateral_triangle, rhombus
brush_size = 5
start_pos = None

# Очистка экрана
screen.fill(WHITE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_b:
                mode = "brush"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_y:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_1:
                current_color = (255, 0, 0)  # Красный
            elif event.key == pygame.K_2:
                current_color = (0, 255, 0)  # Зеленый
            elif event.key == pygame.K_3:
                current_color = (0, 0, 255)  # Синий
            elif event.key == pygame.K_0:
                current_color = (0, 0, 0)
            elif event.key == pygame.K_UP:
                brush_size += 1
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 1)
            elif event.key == pygame.K_ESCAPE:
                screen.fill(WHITE)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if mode == "rect":
                pygame.draw.rect(screen, current_color,
                                 (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif mode == "circle":
                radius = int(math.dist(start_pos, end_pos))
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
            elif mode == "square":
                side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, current_color, (*start_pos, side, side), 2)
            elif mode == "right_triangle":
                pygame.draw.polygon(screen, current_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
            elif mode == "equilateral_triangle":
                side = abs(end_pos[0] - start_pos[0])
                height = (math.sqrt(3) / 2) * side
                pygame.draw.polygon(screen, current_color, [start_pos, (start_pos[0] + side, start_pos[1]),
                                                            (start_pos[0] + side / 2, start_pos[1] - height)], 2)
            elif mode == "rhombus":
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                pygame.draw.polygon(screen, current_color, [
                    (start_pos[0], start_pos[1] - height // 2),
                    (start_pos[0] + width // 2, start_pos[1]),
                    (start_pos[0], start_pos[1] + height // 2),
                    (start_pos[0] - width // 2, start_pos[1])
                ], 2)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size)
            elif mode == "brush":
                pygame.draw.circle(screen, current_color, event.pos, brush_size)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
