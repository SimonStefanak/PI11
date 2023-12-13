import tkinter, time, random
canvas = tkinter.Canvas()
canvas.pack()


stvorec1 = canvas.create_rectangle(10,10,110,110, fill="red")
for i in range(1000):
    canvas.update()
    time.sleep(0.01)
    canvas.move(stvorec1, 1, 1) #stvorec1 je objekt, ktory sa bude posuvat, 100 je o kolko posunut na x osi a 0 o kolko na y
    farba = random.choice(("red", "green", "blue", "yellow"))
    canvas.itemconfig(stvorec1, fill = farba)

canvas.mainloop()