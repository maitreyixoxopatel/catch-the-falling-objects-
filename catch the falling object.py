import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Player settings
player_size = 50
player_color = BLUE
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 7

# Object settings
object_size = 50
object_color = RED
object_speed = 5
object_list = []

# Score
score = 0

# Font
font = pygame.font.SysFont("monospace", 35)

# Function to create a new falling object
def create_object():
    x_pos = random.randint(0, SCREEN_WIDTH - object_size)
    y_pos = 0
    object_list.append([x_pos, y_pos])

# Function to draw the player
def draw_player():
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

# Function to draw objects
def draw_objects():
    for obj in object_list:
        pygame.draw.rect(screen, object_color, (obj[0], obj[1], object_size, object_size))

# Function to update object positions
def update_objects():
    global score
    for obj in object_list:
        obj[1] += object_speed
        if obj[1] > SCREEN_HEIGHT:
            object_list.remove(obj)
            score -= 1
        if (player_x < obj[0] < player_x + player_size or player_x < obj[0] + object_size < player_x + player_size) and \
           (player_y < obj[1] < player_y + player_size or player_y < obj[1] + object_size < player_y + player_size):
            object_list.remove(obj)
            score += 1

# Function to display the score
def display_score():
    score_text = "Score: " + str(score)
    label = font.render(score_text, 1, WHITE)
    screen.blit(label, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 40))

# Main game loop
running = True
clock = pygame.time.Clock()
object_timer = pygame.USEREVENT + 1
pygame.time.set_timer(object_timer, 1000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == object_timer:
            create_object()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < SCREEN_WIDTH - player_size:
        player_x += player_speed

    screen.fill(BLACK)
    draw_player()
    draw_objects()
    update_objects()
    display_score()
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
