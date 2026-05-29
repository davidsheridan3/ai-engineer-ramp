# This game was created using prompt engineering (natural language)

import pygame
import random
import sys

# ----------------------------
# Configuration
# ----------------------------
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (220, 50, 50)
GRAY = (40, 40, 40)
YELLOW = (255, 215, 0)

START_SPEED = 10
MAX_SPEED = 24
SPEED_INCREASE = 1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

font_small = pygame.font.SysFont("arial", 24)
font_medium = pygame.font.SysFont("arial", 32)
font_large = pygame.font.SysFont("arial", 48)


# ----------------------------
# Helpers
# ----------------------------
def draw_text(text, font, color, surface, x, y, center=False):
    render = font.render(text, True, color)
    rect = render.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(render, rect)


def random_food_position(snake):
    while True:
        x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        if (x, y) not in snake:
            return (x, y)


def draw_grid(surface):
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(surface, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(surface, GRAY, (0, y), (WIDTH, y))


def draw_snake(surface, snake):
    for i, segment in enumerate(snake):
        color = DARK_GREEN if i == 0 else GREEN
        rect = pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)


def draw_food(surface, food):
    rect = pygame.Rect(food[0], food[1], GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(surface, RED, rect)
    pygame.draw.rect(surface, BLACK, rect, 1)


def show_start_screen():
    while True:
        screen.fill(BLACK)
        draw_text("SNAKE GAME", font_large, YELLOW, screen, WIDTH // 2, HEIGHT // 2 - 60, center=True)
        draw_text("Use arrow keys to move", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2, center=True)
        draw_text("Press SPACE to start", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 40, center=True)
        draw_text("Press ESC to quit", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 70, center=True)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        clock.tick(30)


def show_game_over_screen(score):
    while True:
        screen.fill(BLACK)
        draw_text("GAME OVER", font_large, RED, screen, WIDTH // 2, HEIGHT // 2 - 60, center=True)
        draw_text(f"Score: {score}", font_medium, WHITE, screen, WIDTH // 2, HEIGHT // 2, center=True)
        draw_text("Press R to restart", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 50, center=True)
        draw_text("Press ESC to quit", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 80, center=True)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        clock.tick(30)


# ----------------------------
# Main Game
# ----------------------------
def game_loop():
    snake = [
        (WIDTH // 2, HEIGHT // 2),
        (WIDTH // 2 - GRID_SIZE, HEIGHT // 2),
        (WIDTH // 2 - 2 * GRID_SIZE, HEIGHT // 2),
    ]
    direction = "RIGHT"
    next_direction = direction
    food = random_food_position(snake)
    score = 0
    speed = START_SPEED

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    next_direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    next_direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    next_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    next_direction = "RIGHT"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        direction = next_direction

        # Move snake
        head_x, head_y = snake[0]
        if direction == "UP":
            head_y -= GRID_SIZE
        elif direction == "DOWN":
            head_y += GRID_SIZE
        elif direction == "LEFT":
            head_x -= GRID_SIZE
        elif direction == "RIGHT":
            head_x += GRID_SIZE

        new_head = (head_x, head_y)

        # Wall collision
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        ):
            return score

        # Self collision
        if new_head in snake:
            return score

        snake.insert(0, new_head)

        # Food collision
        if new_head == food:
            score += 1
            food = random_food_position(snake)
            if speed < MAX_SPEED:
                speed += SPEED_INCREASE
        else:
            snake.pop()

        # Draw everything
        screen.fill(BLACK)
        draw_grid(screen)
        draw_food(screen, food)
        draw_snake(screen, snake)
        draw_text(f"Score: {score}", font_small, WHITE, screen, 10, 10)
        draw_text(f"Speed: {speed}", font_small, WHITE, screen, 10, 35)
        pygame.display.flip()

        clock.tick(speed)

    return score


def main():
    while True:
        show_start_screen()
        score = game_loop()
        show_game_over_screen(score)


if __name__ == "__main__":
    main()