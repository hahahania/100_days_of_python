import colorgram
import turtle as t
import random


def dot_painting(x, y, space):
    for i in range(x):
        for j in range(y):
            pen.pencolor(random.choice(rgb_colors))
            pen.dot(20)
            pen.penup()
            pen.forward(space)
            pen.pendown()

        pen.penup()
        pen.backward(y * space)
        pen.right(90)
        pen.forward(space)
        pen.left(90)
        pen.pendown()


# function counting how many rows and collumns are, space argument is how many space is in betweeen each dot
def count_num(space):
    height = screen.window_height() - 40
    width = screen.window_width() - 40
    x = round(height / space, 0)
    y = round(width / space, 0)
    return int(x), int(y)


colors = colorgram.extract(
    "/Users/haniazwolinska/Desktop/100days_of_python/intermediate_level/tutle_module/hirst painting/image.jpg",
    6,
)
rgb_colors = [(i.rgb.r, i.rgb.g, i.rgb.b) for i in colors]

TURTLE_SIZE = 20
pen = t.Turtle()
screen = t.Screen()
t.colormode(255)
pen.penup()
pen.goto(
    TURTLE_SIZE / 2 - screen.window_width() / 2,
    screen.window_height() / 2 - TURTLE_SIZE / 2,
)
pen.pendown()
pen.speed("fastest")

space = 50

x, y = count_num(space)
dot_painting(x, y, space)

pen.hideturtle()
screen.exitonclick()
