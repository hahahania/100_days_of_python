import turtle as t
from player import Player
from time import sleep
from car import Car
from scoreboard import ScoreBoard

screen = t.Screen()   
screen.setup(600,600)
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()
car_setup = Car()

screen.listen()
screen.onkey(player.move, 'Up')



game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    
    car_setup.create_car()
    car_setup.move()

    for car in car_setup.all_cars:
        if car.distance(player)<25:
            game_on = False
            scoreboard.game_over()

    if player.new_level():
        car_setup.increase_speed()
        scoreboard.new_level()

screen.exitonclick()
