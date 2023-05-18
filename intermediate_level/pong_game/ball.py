from turtle import Turtle 
import random

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x = 0
        self.y = 0

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)

    def bounce(self):
        self.y *= -1

    def hit(self):
        self.x *= -1

    def stop(self):
        self.hideturtle()
        self.x = 0
        self.y = 0
        self.goto(0,0)
        self.showturtle()

    
    def start(self):
        self.x = 10
        self.y = random.randint(-15,15)