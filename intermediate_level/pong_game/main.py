import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep

WIN_WIDTH = 800
WIN_HEIGHT = 600
screen = t.Screen()
screen.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(ball.start, "space")


def paddle_ball_collision():
    if paddle1.distance(ball) < 50 and ball.xcor() < -320 or paddle2.distance(ball) < 50 and ball.xcor() > 320:
        ball.hit()


def ball_wall_collision():
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()


def lost_point():
    if ball.xcor() >= 380:
        ball.stop()
        scoreboard.player1 += 1
        scoreboard.write_score()
    if ball.xcor() <= -380:
        ball.stop()
        scoreboard.player2 += 1
        scoreboard.write_score()


def check_winner():
    if scoreboard.player1 == 5:
        scoreboard.game_over("Player 1")
        return True
    elif scoreboard.player2 == 5:
        scoreboard.game_over("Player 2")
        return True


game_on = True
while game_on:
    screen.update()
    sleep(0.03)
    lost_point()
    ball.move()
    paddle_ball_collision()
    ball_wall_collision()
    if check_winner():
        game_on = False


screen.exitonclick()
