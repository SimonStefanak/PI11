import turtle

def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

t = turtle.Turtle()
t.speed(0)

for j in range(4):
    for i in range(1,201):
        stvorec(2*i)
    t.left(90)

turtle.mainloop()