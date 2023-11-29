import tkinter
import random

canvas = tkinter.Canvas(width=1000, height=600)
canvas.pack()


x = 3
y = 3
d = 50
xx =x
pocet = (1000-2)//(d+5)
stvrtina = d//4
for j in range((600-2)//(d+d//2)):
    for i in range(pocet):
            colors =random.choice( ["blue", "red", "purple"])

            canvas.create_rectangle(x,y+d//2,x+1*d,y+1*d+d//2,fill=colors)
            canvas.create_polygon(x,y+d//2,x+d//2,y,x+1*d,y+d//2,fill=colors,outline="black")
            canvas.create_rectangle(x+stvrtina,y+3*stvrtina,x+stvrtina*3,y+stvrtina*5,fill="light blue")
            canvas.create_line(x+d//2,y+stvrtina*3,x+d//2,y+stvrtina*5)
            canvas.create_line(x+stvrtina,y+d,x+stvrtina*3,y+d)
            x = x+5+d
    y = y+d+d//2
    x =xx
canvas.mainloop()