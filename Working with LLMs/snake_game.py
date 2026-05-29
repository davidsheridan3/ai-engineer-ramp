# This game was created using prompt engineering (natural language)

"""
Snake Game
-----------
Controls:
- Arrow Keys to move
- R to restart after game over

Requirements:
- Python 3 (no external libraries needed)
"""

import turtle
import time
import random

# ==========================================
# WINDOW SETUP
# ==========================================

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Turn off automatic screen updates
# This makes animation smoother
screen.tracer(0)

# ==========================================
# SCORE DISPLAY
# ==========================================

score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

pen.write(
    f"Score: {score}  High Score: {high_score}",
    align="center",
    font=("Arial", 18, "normal")
)

# ==========================================
# CREATE SNAKE HEAD
# ==========================================

head = turtle.Turtle()
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)

# Direction starts stopped
head.direction = "stop"

# ==========================================
# CREATE FOOD
# ==========================================

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# ==========================================
# SNAKE BODY SEGMENTS
# ==========================================

segments = []

# ==========================================
# MOVEMENT FUNCTIONS
# ==========================================

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# ==========================================
# MOVE SNAKE
# ==========================================

def move():

    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)

    elif head.direction == "down":
        head.sety(y - 20)

    elif head.direction == "left":
        head.setx(x - 20)

    elif head.direction == "right":
        head.setx(x + 20)

# ==========================================
# RESET GAME
# ==========================================

def reset_game():
    global score

    # Move head to center
    head.goto(0, 0)
    head.direction = "stop"

    # Remove body segments
    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()

    score = 0

    update_score()

# ==========================================
# UPDATE SCORE DISPLAY
# ==========================================

def update_score():
    pen.clear()

    pen.write(
        f"Score: {score}  High Score: {high_score}",
        align="center",
        font=("Arial", 18, "normal")
    )

# ==========================================
# KEYBOARD CONTROLS
# ==========================================

screen.listen()

screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

screen.onkeypress(reset_game, "r")
screen.onkeypress(reset_game, "R")

# ==========================================
# MAIN GAME LOOP
# ==========================================

delay = 0.1

while True:

    screen.update()

    # -----------------------------
    # Check wall collision
    # -----------------------------
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        reset_game()

    # -----------------------------
    # Check food collision
    # -----------------------------
    if head.distance(food) < 20:

        # Move food to random location
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)

        # Snap to grid
        x = round(x / 20) * 20
        y = round(y / 20) * 20

        food.goto(x, y)

        # Create new body segment
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("green")
        segment.penup()

        segments.append(segment)

        # Increase score
        score += 10

        if score > high_score:
            high_score = score

        update_score()

        # Slightly increase speed
        delay = max(0.05, delay - 0.002)

    # -----------------------------
    # Move body segments
    # -----------------------------
    for index in range(len(segments) - 1, 0, -1):

        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()

        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Move head
    move()

    # -----------------------------
    # Check self collision
    # -----------------------------
    for segment in segments:

        if segment.distance(head) < 20:
            reset_game()
            delay = 0.1
            break

    time.sleep(delay)

# Keep window open
screen.mainloop()