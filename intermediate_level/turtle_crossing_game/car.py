from turtle import Turtle
from turtle import colormode
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

colormode(255)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto((280,random.randint(-270,290)))
        self.color(random_color())

    def move(self, vel):
        self.forward(vel)

