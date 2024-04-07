
import tkinter as tk
import random

POINTS1 = 0
POINTS2 = 0


def move_object1():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.coords(object1, x, y, x + 20, y + 20)

    if x <= 0:
        global POINTS1
        POINTS1 += 1
        canvas.itemconfig(label1, text="Points: " + str(POINTS1))

    root.after(1000, move_object1)


def move_object2(event):
    x = event.x
    y = event.y
    canvas.coords(object2, x, y, x + 20, y + 20)

    global POINTS2
    global POINTS1
    if (x >= canvas.coords(object1)[0] and x <= canvas.coords(object1)[2]) and (
            y >= canvas.coords(object1)[1] and y <= canvas.coords(object1)[3]):
        POINTS2 += 1
        canvas.itemconfig(label2, text="Points: " + str(POINTS2))


root = tk.Tk()
root.title("Objects Game")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

label1 = canvas.create_text(50, 380, text="Points: 0", anchor="w")
label2 = canvas.create_text(350, 380, text="Points: 0", anchor="e")

object1 = canvas.create_oval(0, 0, 20, 20, fill="red")
object2 = canvas.create_oval(190, 190, 210, 210, fill="blue")

move_object1()

canvas.bind("<Motion>", move_object2)

root.mainloop()