import tkinter

def klik(event):
    x, y = event.x, event.y
    canvas.create_line(10, 10, x, y)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind("<ButtonPress>", klik)

tkinter.mainloop()