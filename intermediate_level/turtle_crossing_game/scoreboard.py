from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 260)
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center",
            font=("candara", 20, "bold"))
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"You lost. You've reached {self.level} level", align="center",
            font=("candara", 24, "bold"))
        
    def new_level(self):
        self.level+=1
        self.write_score()
