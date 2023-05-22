import turtle as t
from player import Player
from time import sleep
from car import Car

screen = t.Screen()   
screen.setup(600,600)
screen.tracer(0)

player = Player()

levels = {1:[20,15], 2:[30,15], 3:[30,20], 4:[35,20], 5:[40,20]}

def create_cars(amount):
    cars = []
    for _ in range(amount):
        cars.append(Car())
    return cars

screen.listen()
screen.onkey(player.move, 'Up')

game_on = True
while game_on:
    screen.update()


screen.exitonclick()
