import random
import turtle

t = turtle.Turtle()
turtle.delay(0)

def slnko(p, v):
    t.begin_fill()
    t.color("gold")
    t.dot(v)
    t.end_fill()
    for i in range(p):
        t.pensize(10)
        t.begin_fill()
        t.color("gold")
        t.fd(v)
        t.end_fill()
        t.penup()
        t.bk(v)
        t.pendown()
        t.rt(360/p)




slnko(25,150)


turtle.mainloop()
