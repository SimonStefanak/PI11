import turtle

t = turtle.Turtle()
turtle.delay(0)

def obluk(d):
    for i in range(9):
        t.fd(d)
        t.lt(10)


def lupen(d):
    for i in range(2):
        obluk(d)
        t.lt(90)



def kvet(n, d):
    for i in range(n):
        lupen(d)
        t.lt(360 / n)

kvet(100, 30)


turtle.mainloop()
