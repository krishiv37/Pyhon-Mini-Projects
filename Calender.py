import calendar
from tkinter import*

def display():
    m = int(month.get())
    y = int(year.get())
    c = calendar.month(y,m)
    t1.delete(0.0,END)
    t1.insert(INSERT, c)


window = Tk()
window.title("Calender")
window.geometry("400x400")

l1 = Label(window, text = "Month")
l1.grid(row = 0, column = 0)
l2 = Label(window, text = "Year")
l2.grid(row = 0, column = 1)
month = Spinbox(window,from_=1, to = 12, width = 8)
month.grid(row = 1, column = 0, padx = 5)
year = Spinbox(window,from_ = 2000, to = 2100)
year.grid(row = 1, column = 1, padx = 5)
b1 = Button(window, text= "Show Calender", height = 3, command=display)
b1.grid(row = 10, column = 0,padx = 10)
t1 = Text(window,height=8,width=20)
t1.grid(row= 3, column=0)

window.mainloop()