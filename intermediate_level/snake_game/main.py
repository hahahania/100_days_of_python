# STEPS
# CREATE SNAKE BODY
# MOVE WITH ARROWS
# CREATE POINT
# ADDING NEW PART OF SNAKE AFTER EATING POINTS
# COUNTING SCORE
# LOOSING WHEN SNAKES BODY OR WALL IS TOUCHED

import turtle as t
from time import sleep

score = 0
snake = t.Turtle("square")
snake.penup()
snake.color("red")

screen = t.Screen()
screen.screensize(600, 600)
screen.bgcolor("black")

food = t.Turtle()
food.shape("circle")
food.color("blue")

pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 290)
pen.write(f"Score : {score}", align="center", font=("candara", 24, "bold"))


def up():
    if snake.heading() != 270:
        snake.setheading(90)


def left():
    if snake.heading() != 0:
        snake.setheading(180)


def right():
    if snake.heading() != 180:
        snake.setheading(0)


def down():
    if snake.heading() != 90:
        snake.setheading(270)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(down, "Down")

game = True
while game:
    snake.forward(10)
    sleep(0.03)
screen.exitonclick()
