import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()


r = 5


for i in range(10000):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if y < 90:
        farba = "black"
    elif y < 170:
        farba = "red"
    else:
        farba = "gold"
    canvas.create_oval(x-r, y-r, x+r, y+r, fill= farba)




canvas.mainloop()