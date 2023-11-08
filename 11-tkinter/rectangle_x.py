import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x = 40
y = 30
d = 20
farba = "magenta"

canvas.create_rectangle(x, y, x+d, y+d, fill=farba)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill=farba)
canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill=farba)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill=farba)
canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=farba)
canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill=farba)
canvas.create_rectangle(x+3*d, y+d, x+4*d, y+2*d, fill=farba)
canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d, fill=farba)
canvas.create_rectangle(x, y+4*d, x+d, y+5*d, fill=farba)

x = 8 * d
y = 30
d = 20
farba = "green"

canvas.create_rectangle(x, y, x+d, y+d, fill=farba)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill=farba)
canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill=farba)
canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill=farba)
canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=farba)
canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill=farba)
canvas.create_rectangle(x+3*d, y+d, x+4*d, y+2*d, fill=farba)
canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d, fill=farba)
canvas.create_rectangle(x, y+4*d, x+d, y+5*d, fill=farba)

canvas.mainloop()