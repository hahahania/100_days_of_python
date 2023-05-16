# STEPS
# CREATE SNAKE BODY
# MOVE WITH ARROWS
# CREATE POINT
# ADDING NEW PART OF SNAKE AFTER EATING POINTS
# COUNTING SCORE
# LOOSING WHEN SNAKES BODY OR WALL IS TOUCHED

import turtle as t
from time import sleep
from snake import Snake

screen = t.Screen()
screen.screensize(600, 600)
screen.bgcolor("black")

food = t.Turtle()
food.shape("circle")
food.color("blue")

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game = True
while game:
    screen.update()
    sleep(0.05)
    snake.move()


screen.exitonclick()
