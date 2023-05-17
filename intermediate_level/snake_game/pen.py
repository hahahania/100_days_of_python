import turtle as t
class Pen:
    def __init__(self):
        self.pen = None
        self.create()

    def create(self):
        self.pen = t.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 280)
        self.write_score(0)

    def write_score(self,score):
        self.pen.clear()
        self.pen.write(f"Score : {score}", align="center",
            font=("candara", 24, "bold"))
