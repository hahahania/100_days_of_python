from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

def forward():
    tim.fd(10)
def backward():
    tim.bk(10)
def counter_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def clear():
    tim.setpos((0.0,0.0))
    tim.clear()
    

tim.speed('fastest')
screen.onkey(forward,'w')
screen.onkey(backward,'s')
screen.onkey(counter_clockwise,'a')
screen.onkey(clockwise,'d')
screen.onkey(clear, 'c')
screen.exitonclick()
