import pygame
import sys

# Initialize Pygame
pygame.init()

# Game settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Game')

# Colors
black = (0, 0, 0)
blue = (0, 128, 255)

# Player settings
player_size = 50
player_pos = [width // 2, height - 2 * player_size]
player_speed = 5

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get all the keys currently pressed
    keys = pygame.key.get_pressed()

    # Move the player
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < height - player_size:
        player_pos[1] += player_speed

    # Fill the screen with black
    screen.fill(black)

    # Draw the player
    pygame.draw.rect(screen, blue, (player_pos[0], player_pos[1], player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate (60 FPS)
    clock.tick(60)
