from turtle import Turtle

STARTING_POS = (0,-290)
MOVE_DISTANCE = 10
FINISH = 290
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.set_up()
        self.setheading(90)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def set_up(self):
        self.goto(STARTING_POS)

    def new_level(self):
        if self.ycor()>FINISH:
            self.set_up()
            return True
        

    