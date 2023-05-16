import turtle as t
from random import randint
class Food():
    def __init__(self) -> None:
        self.x_cor = 0 
        self.y_cor = 0

    def create(self):
        self.x_cor = randint(-270,270)
        self.y_cor = randint(-270,270)
        food = t.Turtle('circle')
        food.color('blue')
        food.penup()
        food.goto((self.x_cor,self.y_cor))
    
    