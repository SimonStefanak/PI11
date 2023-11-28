import tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()
height = 600
width = 1000

x = 3
y = 3
d = 50
xx =x
pocet = (width-2)//(d+5)
stvrtina = d//4
# // celociselne delenie
# napr 7 // 3 = 2
for g in range((height-2)//(d+d//2)):
    for i in range(pocet):
            colors =random.choice( ["blue", "red", "purple"])

            canvas.create_rectangle(x,y+d//2,x+1*d,y+1*d+d//2,fill=colors)
            canvas.create_polygon(x,y+d//2,x+d//2,y,x+1*d,y+d//2,fill="crimson",outline="black")
            canvas.create_rectangle(x+stvrtina,y+3*stvrtina,x+stvrtina*3,y+stvrtina*5,fill="sky blue")
            canvas.create_line(x+d//2,y+stvrtina*3,x+d//2,y+stvrtina*5)
            canvas.create_line(x+stvrtina,y+d,x+stvrtina*3,y+d)
            x = x+5+d
    y = y+d+d//2
    x =xx
canvas.mainloop()