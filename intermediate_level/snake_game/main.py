import turtle as t
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

WIN_WIDTH = 600
WIN_HEIGHT = 600

food = Food()
snake = Snake()
scoreboard = ScoreBoard()
score = 0

screen = t.Screen()
screen.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
screen.bgcolor("black")


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


def food_collision():
    if snake.head.distance(food.food) < 20:
        food.move_food()
        snake.add_segment()
        snake.score += 1
        scoreboard.write_score(snake.score)


def wall_collision():
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.last_message(snake.score)
        return True


def tail_collision():
    for segment in snake.segments:
        if segment == snake.head:
            pass
        else:
            if snake.head.distance(segment) < 15:
                scoreboard.last_message(snake.score)
                return True


if __name__ == "__main__":
    game = True
    while game:
        screen.update()
        sleep(0.005)
        snake.move()

        food_collision()
        if wall_collision():
            game = False
        if tail_collision():
            game = False

    screen.exitonclick()
