import random
import turtle

t = turtle.Turtle()
turtle.delay(0)

def obluk(d):
    for i in range(9):
        t.fd(d)
        t.lt(10)

def lupen(d):
    for i in range(2):
        t.fillcolor(farba)
        t.begin_fill()
        obluk(d)
        t.lt(90)
        t.end_fill()

x = random.randint(-200, 200)
y = random.randint(-200, 200)
def kvet(n, d):
    for i in range(n):
        lupen(d)
        t.lt(360 / n)



for i in range(5):
    kvet(10, 5)
    t.penup()
    t.setpos(x, y)
    t.pendown()

turtle.mainloop()