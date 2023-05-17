# COUNTING SCORE
# LOOSING WHEN SNAKES BODY OR WALL IS TOUCHED

import turtle as t
from time import sleep
from snake import Snake
from food import Food
from pen import Pen

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

pen = Pen()


score = 0


def food_collision():
    if snake.head.distance(food.food) < 20:
        food.move_food()
        snake.add_segment()
        snake.score += 1
        pen.write_score(score = snake.score)

game = True
while game:
    screen.update()
    sleep(0.005)
    food_collision()
    snake.move()



screen.exitonclick()
