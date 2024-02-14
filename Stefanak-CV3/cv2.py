import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()


for i in range(10):
    x = random.randint(50, 300)
    y = random.randint(50, 200)
    canvas.create_rectangle(x, y, x+100, y+40, fill="light grey")
    canvas.create_text(x, y, text="python", font="arial 14")
  


canvas.mainloop()