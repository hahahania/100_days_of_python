import turtle as t
from random import randint


class Food:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.food = None
        self.create()

    def move_food(self):
        self.x = randint(-270, 270)
        self.y = randint(-270, 270)
        self.food.goto((self.x,self.y))

    def create(self):
        self.food = t.Turtle("circle")
        self.food.color("blue")
        self.food.penup()
        self.move_food()


    