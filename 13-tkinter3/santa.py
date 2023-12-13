import tkinter, time, random

canvas_width = 600
canvas_height = 600
santa_x = c
santa_y = 66
santa_posun = 1

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

image_santa = tkinter.PhotoImage(file="santa.png")
santa = canvas.create_image(santa_x, santa_y, image=image_santa)
santa1 = canvas.create_image(64, 64, image=image_santa)
santa2 = canvas.create_image(512, 64, image=image_santa)
while True:
    canvas.update()
    time.sleep(0.01)
    canvas.move(santa, 0, santa_posun)
    canvas.move(santa1, santa_posun, 0)
    canvas.move(santa2, 0, santa_posun)
    santa_y = santa_y + santa_posun
    if santa_y == canvas_height + 66:
        canvas.delete(santa)
        santa_y = 66
        santa = canvas.create_image(santa_x, santa_y, image=image_santa)
        santa1 = canvas.create_image(64, 64, image=image_santa)
    if santa2 == canvas_height + 66:
        canvas.move(santa2, 0, -1)







canvas.mainloop()