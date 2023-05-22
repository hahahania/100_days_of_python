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

STARTING_MOVE_DISTANCE = 5
MOVE_INCREAMENT = 10

class Car():
    def __init__(self):
        self.all_cars = []
        self.vel = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = random.randint(1,6)
        if random_num == 6:
            car = Turtle('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.goto((280,random.randint(-250,280)))
            car.color(random_color())
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.vel)

    def increase_speed(self):
        self.vel += MOVE_INCREAMENT

    def game_over(self,player):
        for car in self.all_cars:
            return True if car.distance(player)<25 else False
