import turtle

pocet = 4
turtles = [] #list (resp. pole) korytnaciek

for i in range(pocet):
    t = turtle.Turtle()
    t.penup()
    t.setpos(i * 100, 0)
    t.pendown()
    turtles.append(t)

for i in range(4):
    for t in turtles:
        t.fd(50)
        t.rt(90)

turtle.mainloop()
