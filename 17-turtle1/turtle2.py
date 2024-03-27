import random
import turtle
t = turtle.Turtle()
t.speed(0)



def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

x = 0
y = -10
for j in range(8):
    for i in range(7):
        if (i + j)/2 == 0:
            color = "yellow"
        else:
            color = "red"
        t.fillcolor(color)
        t.begin_fill()
        stvorec(10)
        t.end_fill()
        t.penup()
        t.forward(10)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        stvorec(10)
        t.end_fill()
    t.penup()
    t.setpos(x, y)
    t.pendown()
    y = y - 10







turtle.mainloop()