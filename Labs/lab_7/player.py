import pygame
import os



pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spotify Player Clone")


BLACK = (18, 18, 18)
GREEN = (30, 215, 96)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)


playlist = [
    "/Users/alikhan/PycharmProjects/PP2_Alikhan/Labs/lab_7/songs/Dreamcatcher.mp3",
    "/Users/alikhan/PycharmProjects/PP2_Alikhan/Labs/lab_7/songs/Impossible.mp3",
    "/Users/alikhan/PycharmProjects/PP2_Alikhan/Labs/lab_7/songs/MariaImDrunk.mp3"
]

current_track = 0
playing = False



def play_music():
    global playing
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    playing = True


def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()


def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()


def toggle_pause():
    global playing
    if playing:
        pygame.mixer.music.pause()
        playing = False
    else:
        pygame.mixer.music.unpause()
        playing = True



def draw_ui():
    screen.fill(BLACK)
    pygame.draw.rect(screen, GRAY, (50, 200, 300, 50), border_radius=25)
    pygame.draw.circle(screen, GREEN, (100, 225), 20)
    pygame.draw.circle(screen, GREEN, (200, 225), 20)
    pygame.draw.circle(screen, GREEN, (300, 225), 20)

    font = pygame.font.Font(None, 36)
    text = font.render("Now Playing: " + os.path.basename(playlist[current_track]), True, WHITE)
    screen.blit(text, (50, 100))

    pygame.display.flip()


running = True
while running:
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                toggle_pause()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                prev_track()

pygame.quit()