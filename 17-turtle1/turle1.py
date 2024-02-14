import random
import turtle



def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)


t = turtle.Turtle()
t.speed(0)



for i in range(30):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    stvorec(30)
    t.penup()
    t.setpos(x, y)
    t.seth(random.randint(0, 359))
    t.pendown()
    t.fillcolor(random.choice(("red", "green", "blue", "yellow"))
    t.begin_fill()
    stvorec(30)
    t.end_fill()






turtle.mainloop()