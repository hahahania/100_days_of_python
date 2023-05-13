import turtle as t


tim = t.Turtle()
win = t.Screen()


drawing = True
angle = 0
tim.speed('fastest')
while drawing:
    if angle == 360:
        drawing = False
    tim.setheading(angle)
    tim.circle(100)
    angle += 5

win.exitonclick()