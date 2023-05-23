import turtle as t
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

WIN_WIDTH = 600
WIN_HEIGHT = 600
path = '/Users/haniazwolinska/Desktop/100days_of_python/intermediate_level/snake_game/snake_scores.txt'

highscores = open(path, 'a+')
scoreboard = ScoreBoard(highscores)

food = Food()
snake = Snake()

screen = t.Screen()
screen.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


def food_collision():
    if snake.head.distance(food.food) < 20:
        food.move_food()
        snake.add_segment()
        scoreboard.score += 1
        scoreboard.write_score()


def wall_collision():
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -295
        or snake.head.ycor() > 295
        or snake.head.ycor() < -290
    ):
        scoreboard.last_message()
        return True


def tail_collision():
    for segment in snake.segments:
        if segment == snake.head:
            pass
        else:
            if snake.head.distance(segment) < 15:
                scoreboard.last_message()
                return True


if __name__ == "__main__":
    game = True
    while game:
        screen.update()
        sleep(0.1)
        snake.move()

        food_collision()
        if wall_collision():
            game = False
            scoreboard.new_highscore(highscores)
        if tail_collision():
            game = False
            scoreboard.new_highscore(highscores)

    screen.exitonclick()
