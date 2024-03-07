from tkinter import *

window  = Tk()
window.config(width = 700, height = 300)
window.configure(background = "light green")

def greet(word):
    Label(window, text = word, font = ("Arial",20,"bold")).pack()

def canvas_text(event):
    for i in range(0,100,10):
        canvas.create_text(event.x+i, event.y+i, text = "Python is fun", fill = "Red")

def show(event):
    Label(window, text = "Mouse Entered", font = ("Arial",20,"bold")).pack()

def show1(event):
    Label(window, text = "Mouse Left", font = ("Arial",20,"bold")).pack()

canvas = Canvas(window, width = 300, height = 300, background = "dark grey")
canvas.pack()
canvas.create_rectangle(20,20,60,60, fill = "Blue")
canvas.create_arc(100,20,200,200, extent = 270, fill = "yellow")

button = Button(window, text = "ENTER")
button.pack()
button.bind("<Enter>",show)
canvas.bind("<Leave>", show1)

window.bind("<w>",lambda event : greet("hello"))
canvas.bind("<Button-1>",canvas_text)

window.mainloop()