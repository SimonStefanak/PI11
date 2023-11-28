import tkinter

canvas = tkinter.Canvas()
canvas.pack()
x = 5
y = 5
d = 10

canvas.create_rectangle(x, y, x + d, y + d)
canvas.create_rectangle(x + d, y, x + 2 * d, y + d)


canvas.mainloop()