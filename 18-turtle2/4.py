import turtle
turtle.delay(0)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.penup()
t1.setpos(-100, 0)
t1.pendown()

t2.penup()
t2.setpos(100, 0)
t2.pendown()

t3.penup()
t3.setpos(0, 100)
t3.pendown()

def stvorec(dlzka):
    for i in range(4):
        t1.fd(dlzka)
        t2.fd(dlzka)
        t3.fd(dlzka)
        t1.lt(90)
        t2.lt(90)
        t3.lt(90)

n = 50

for i in range(n):
    stvorec(100)
    t1.lt(360 / n)
    t2.lt(360 / n)
    t3.lt(360 / n)









turtle.mainloop()