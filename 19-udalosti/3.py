import tkinter
import random

def klik(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red")
def tahaj(event):
    x, y = event.x, event.y
    canvas.create_oval(x-10, y-10, x+10, y+10, fill =))


canvas = tkinter.Canvas()
canvas.pack()
canvas.bind("<B1-Motion>", tahaj)
canvas.bind("<ButtonPress>", klik)

canvas.mainloop()