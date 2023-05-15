import turtle as t
import random

screen = t.Screen()
screen.setup(width=700, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for i in range(0, 6):
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto((-330, starting_positions[i]))
    turtles.append(turtle)

user_choice = screen.textinput(
    title="CHOOSE TURTLE",
    prompt="Which turtle will win the race? (red,orange,yellow,green,blue or purple): ",
)

race = True

if user_choice:
    race = True

while race:
    for i in turtles:
        if i.xcor() > 330:
            race = False
            winner_color = i.pencolor()
            if winner_color == user_choice:
                print(
                    f"Congratulations, you won! The turtle which won is {winner_color} turtle!"
                )
            else:
                print(
                    f"You lost, you chose {user_choice} turtle and the winner is {winner_color} turtle"
                )
        pace = random.randint(0, 10)
        i.fd(pace)

screen.exitonclick()
