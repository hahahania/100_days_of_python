from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(position)

    def up(self):
        if self.ycor()<250:
             self.goto(self.xcor(),self.ycor()+25)
    
    def down(self):
        if self.ycor()>-250:
            self.goto(self.xcor(),self.ycor()-25)
