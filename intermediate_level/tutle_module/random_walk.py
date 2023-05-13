import turtle as t
import random


def is_in_screen(window, turtle):
    left_side = -(window.window_width() / 2)
    rifht_side = window.window_width() / 2
    top = window.window_height() / 2
    bottom = -(window.window_height() / 2)

    x_cor = turtle.xcor()
    y_cor = turtle.ycor()

    correct = True
    if x_cor < left_side or x_cor > rifht_side:
        correct = False
    if y_cor < bottom or y_cor > top:
        correct = False
    return correct

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

skiper = t.Turtle()
skiper.pensize(7)
t.colormode(255)
skiper.hideturtle()

screen = t.Screen()


while is_in_screen(screen, skiper):
    direction = random.choice([0, 1])
    if direction == 0:
        skiper.left(90)
    else:
        skiper.right(90)
    skiper.pencolor(random_color())
    skiper.forward(random.randint(40, 60))



