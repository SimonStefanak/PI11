import random
import turtle

t = turtle.Turtle()
turtle.delay(0)

def terc(p):
    d = 15 * p
    t.dot(d)
    color1 = "blue"
    color2 = "yellow"
    for i in range(p):
        t.begin_fill()
        t.color(color1)
        t.dot(d)
        t.end_fill()
        d = d-15
        color1, color2 = color2, color1


terc(20)

turtle.mainloop()