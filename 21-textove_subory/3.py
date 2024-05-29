import tkinter

canvas= tkinter.Canvas()
canvas.pack()

fbody = open("body.txt", "r")
for riadok in fbody:
    medzera = riadok.find(" ")
    x = int(riadok[:medzera])
    y = int(riadok[medzera:])
    print(x, y)
    print(type(x))

canvas.crea


tkinter.mainloop()