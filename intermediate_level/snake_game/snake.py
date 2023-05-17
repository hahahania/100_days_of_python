import turtle as t

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.score = 0

    def add_segment(self):
        segment = t.Turtle("square")
        segment.hideturtle()
        segment.penup()
        segment.color("red")
        segment.goto(self.segments[-1].xcor(),self.segments[1].ycor())
        segment.showturtle()
        self.segments.append(segment)

    def create_snake(self):
        for pos in STARTING_POS:
            segment = t.Turtle("square")
            segment.penup()
            segment.color("red")
            segment.goto(pos)
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto((new_x, new_y))
        self.head.fd(MOVE_DISTANCE)
    

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

