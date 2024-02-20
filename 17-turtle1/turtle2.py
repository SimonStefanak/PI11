import random
import turtle
t = turtle.Turtle()
t.speed(0)



def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

color1 = "yellow"
color2 = "red"
x = 0
y = -10
for j in range(8):
    for i in range(1,8):
        t.fillcolor(color1)
        t.begin_fill()
        stvorec(10)
        t.end_fill()
        t.penup()
        t.forward(10)
        t.pendown()
        stvorec(10)
        color1 = color2
    t.penup()
    t.setpos(x, y)
    t.pendown()
    color2 = color1
    y = y - 10






turtle.mainloop()