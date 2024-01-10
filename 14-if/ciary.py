import tkinter
canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()

width = 600
height = 500
x = 0
y = 0
d = 25
pocet = 598//d
pocet2 = 498//d
farba1 = "red"
farba2 = "blue"

for j in range(pocet2):
        canvas.create_line(x, y+d, height, y+d, fill=farba1)
        farba1, farba2 = farba2, farba1
for i in range(pocet):
        canvas.create_line(x+d, y, x+d, height, fill=farba1)
        x = x + d
        farba1, farba2 = farba2, farba1





canvas.mainloop()