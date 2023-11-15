import tkinter
import random
canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()

x = 100
y = 100
d = 50
b = d // 2
c = d // 4

for i in range (3):
    canvas.create_rectangle(x, y, x + d, y + d)
    canvas.create_rectangle(x+3*c, y+3*c, x+c, y+c)
    canvas.create_line(x, y, y+b, x-b)
    canvas.create_line(y+b, x-b, y+d, x)
    x = x + d
    b = b + d






canvas.mainloop()