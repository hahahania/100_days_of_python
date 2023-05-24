import turtle as t
import pandas 

pic = 'blank_states_img.gif'

screen = t.Screen()
screen.addshape(pic)
t.shape(pic)

pen = t.Turtle()
pen.penup()
pen.hideturtle()


data = pandas.read_csv('50_states.csv')
states = data.state

guessed_states = []

while len(guessed_states)<50:
    answer = t.textinput(f'{len(guessed_states)}/50 US States', 'Enter name of the state: ').title()
    if answer == 'Exit':
        unguessed = []
        for state in states:
            if state not in guessed_states:
                unguessed.append(state)
        to_learn = pandas.DataFrame(unguessed)
        to_learn.to_csv('states_to_learn.csv')
        break
    
    if (states.eq(answer)).any():
        guessed_states.append(answer)
        chosen_state = data[data.state==answer]
        pen.goto(int(chosen_state.x),int(chosen_state.y))
        pen.write(answer)




screen.exitonclick()