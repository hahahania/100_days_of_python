import turtle as t

class ScoreBoard():
    def __init__(self) -> None:
        self.pen = None
        self.player1 = 0
        self.player2 = 0
        self.create()
        self.middle()

    def create(self):
        self.pen = t.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.write_score()

    def write_score(self):
        self.pen.clear()
        self.pen.write(f"Player 1 : {self.player1}          Player 2 : {self.player2}", align="center",
            font=("candara", 20, "bold"))
    
    def middle(self):
        y = 300
        new_pen = t.Turtle()
        new_pen.goto(0,y)
        for i in range(20):
            y-=15
            new_pen.pencolor('white')
            new_pen.goto(0,y)
            new_pen.penup()
            y-=15
            new_pen.goto(0,y)
            new_pen.pendown()
        
    def game_over(self,winner_name):
        self.pen.clear()
        self.pen.goto(0,0)
        self.pen.write(f"The winner is: {winner_name}", align="center",font=("candara", 24, "bold"))