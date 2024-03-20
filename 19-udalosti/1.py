import random
import tkinter




def vypis():
    text = "Python"
    x = random.randrange(1, 600)
    y = random.randrange(1, 600)
    canvas.create_text(x, y, text=text, font="arial 20")

def zmaz():
    canvas.delete("all")

canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()
tkinter.Button(text = "vypis", command=vypis).pack()
tkinter.Button(text = "zmaz", command=zmaz).pack()

vypis()


canvas.mainloop()

