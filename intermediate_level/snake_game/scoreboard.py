import turtle as t
class ScoreBoard:
    def __init__(self,file):
        self.pen = None
        self.score = 0
        self.highscore = 0
        self.get_highscore(file)
        self.create()


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
        self.pen.write(f"Score : {self.score}, Highscore : {self.highscore}", align="center",
            font=("candara", 20, "bold"))

    def last_message(self):
        self.pen.clear()
        self.pen.goto(0,0)
        self.pen.write(f"You lost. Your final score : {self.score}", align="center",
            font=("candara", 24, "bold"))
        
    def get_highscore(self, file):
        file.seek(0)
        scores = file.readlines()
        self.highscore = int(scores[-1])
        
    def new_highscore(self, file):
        if self.score>self.highscore:
            file.write('\n'+str(self.score))