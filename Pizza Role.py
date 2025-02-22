import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Load assets
pizza_roll_img = pygame.image.load("pizza_roll.png")
pizza_roll_img = pygame.transform.scale(pizza_roll_img, (100, 100))

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pizza Roll Clicker")

# Game variables
score = 0
click_power = 1
pizza_x = WIDTH // 2 - 50
pizza_y = HEIGHT // 2 - 50

# Font
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw pizza roll
    screen.blit(pizza_roll_img, (pizza_x, pizza_y))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if pizza_x < mx < pizza_x + 100 and pizza_y < my < pizza_y + 100:
                score += click_power
    
    pygame.display.flip()

pygame.quit()
