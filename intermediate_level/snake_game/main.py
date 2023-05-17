# CREATE POINT
# ADDING NEW PART OF SNAKE AFTER EATING POINTS
# COUNTING SCORE
# LOOSING WHEN SNAKES BODY OR WALL IS TOUCHED

import turtle as t
from time import sleep
from snake import Snake
from food import Food

snake = Snake()
food = Food()

screen = t.Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

score = 0

def food_collision(snake:snake,food:food):
    if snake.head.distance(food.food) < 20:
        food.move_food()


game = True
while game:
    screen.update()
    sleep(0.05)
    food_collision(snake,food)
    snake.move()


screen.exitonclick()
