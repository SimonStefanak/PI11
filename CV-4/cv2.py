import random
import turtle

t = turtle.Turtle()
turtle.delay(0)

def slnko(p, v):
    t.begin_fill()
    t.color("yellow")
    t.dot(v)
    t.end_fill()
    for i in range(p):
        t.pensize(10)
        t.begin_fill()
        t.color("yellow")
        t.fd(v)
        t.end_fill()
        t.penup()
        t.bk(v)
        t.pendown()
        t.rt(360/p)




slnko(20,100)


turtle.mainloop()
