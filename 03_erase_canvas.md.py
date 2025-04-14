import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 40
ERASER_SIZE = 50
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BG_COLOR = (200, 200, 200)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")

# Create grid of cells
cols = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE
cells = [[BLUE for _ in range(cols)] for _ in range(rows)]

# Main loop
clock = pygame.time.Clock()
running = True
dragging = False

while running:
    screen.fill(BG_COLOR)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser_rect = pygame.Rect(mouse_x, mouse_y, ERASER_SIZE, ERASER_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    # Draw and possibly erase cells
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if dragging and eraser_rect.colliderect(rect):
                cells[row][col] = WHITE
            pygame.draw.rect(screen, cells[row][col], rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # cell border

    # Draw eraser (transparent red box)
    pygame.draw.rect(screen, (255, 0, 0, 100), eraser_rect, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
