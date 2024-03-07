from tkinter import *

def find_xy(event):
    global current_x, current_y
    current_x = event.x
    current_y = event.y

def draw(event):
    global current_x, current_y
    global line
    canvas.create_line(current_x,current_y,event.x,event.y,fill = color,width=pensize)
    current_x = event.x
    current_y = event.y

def change_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete("all")
    color_palette()

def increase_pensize():
    global pensize
    pensize = 10

def decrease_pensize():
    global pensize
    pensize = 1

def use_eraser():
    global color
    color = canvas["background"]

color = "black"
pensize = 1

window = Tk()
window.title("Paint")
window.config(bg = "white")
window.state("zoomed")
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

canvas = Canvas(window)
canvas.grid(row = 0, column = 0, sticky = "nsew")
canvas.bind("<Button-1>",find_xy)
canvas.bind("<B1-Motion>", draw)

menubar = Menu(window)
window.config(menu = menubar)

submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Clear Frame", menu=submenu)
submenu.add_command(label="New Canvas", command=new_canvas)

brushmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Pen Size",menu = brushmenu)
brushmenu.add_command(label="Increase", command=increase_pensize)
brushmenu.add_command(label="Decrease",command=decrease_pensize)

submenu.add_command(label = "Erase", command=use_eraser)

def color_palette():
    clr = canvas.create_rectangle(10,10,30,30, fill = "blue")
    canvas.tag_bind(clr,"<Button-1>",lambda x : change_color("blue"))
    clr = canvas.create_rectangle(10,40,30,60, fill = "red")
    canvas.tag_bind(clr,"<Button-1>",lambda x : change_color("red"))
    clr = canvas.create_rectangle(10,70,30,90, fill = "green")
    canvas.tag_bind(clr,"<Button-1>",lambda x : change_color("green"))
    clr = canvas.create_rectangle(10,100,30,120, fill = "yellow")
    canvas.tag_bind(clr,"<Button-1>",lambda x : change_color("yellow"))
    clr = canvas.create_rectangle(10,130,30,150, fill = "black")
    canvas.tag_bind(clr,"<Button-1>",lambda x : change_color("black"))
    clr = canvas.create_rectangle(10,160,30,180, fill = "pink")
    canvas.tag_bind(clr,"<Button-1>",lambda x : change_color("pink"))

color_palette()

window.mainloop()