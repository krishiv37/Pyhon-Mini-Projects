from tkinter import*
from tkinter import messagebox

def login():
    if entrybox1.get()=="Email/Username" or entrybox1.get()=="" or entrybox2.get()=="Password" or entrybox2.get()=="":
        messagebox.showerror("Error","Username or Password\ncannot be empty")
    else:
        user = entrybox1.get()
        pwd = entrybox2.get()
        data = []
        found = False
        with open("Logindatabase.txt","r")as f:
            filecontent = f.read()
            data = filecontent.split("\n")
        for i in range(len(data)-1):
            if user in data:
                if data[i]==user and data[i+1]==pwd:
                    found = True
        if found:               # Boolean variables can be used as conditions
            messagebox.showinfo("Success","Logged in Successfully")
        else:
            if user not in data:
                messagebox.showerror("Error","Incorrect Username")
            else:
                messagebox.showerror("Error","Incorrrect Password")

def signup():
    if entrybox1.get()=="Email/Username" or entrybox1.get()=="" or entrybox2.get()=="Password" or entrybox2.get()=="":
        messagebox.showerror("Error","Username or Password\ncannot be empty")
    else:
        user = entrybox1.get()
        pwd = entrybox2.get()
        with open("Logindatabase.txt","a")as f:
            f.write(user+"\n")
            f.write(pwd+"\n")
        messagebox.showinfo("Success","Signed up Successfully")

def forgot_password():
    screen = Toplevel(window)
    screen.title("Forgot Password")
    screen.geometry("250x250")
    screen.resizable(0,0)
    screen.config(background="white")
    label1 = Label(screen, text = "Forget Password", bg = "white", fg = "blue",font=("Times",20,"bold italic"))
    label1.place(x=30,y=20)
    entrybox3 = Entry(screen,width=30,font=("Times",15,"normal"))
    entrybox3.place(x=20,y=70)
    entrybox3.insert(0,"Email/Username")
    entrybox4 = Entry(screen, width=30,font=("Times",15,"normal"))
    entrybox4.place(x=20,y=100)
    entrybox4.insert(0,"Password")


    def on_enter3(e):
        entrybox3.delete(0,END)

    def on_leave3(e):
        name = entrybox3.get()
        if name == "":
            entrybox3.insert(0,"Email/Username")

    def on_enter4(event):
            entrybox4.delete(0,END)

    def on_leave4(event):
        name = entrybox4.get()
        if name == "":
            entrybox4.insert(0,"Password")
    entrybox3.bind("<FocusIn>",on_enter3)
    entrybox3.bind("<FocusOut>",on_leave3)
    entrybox4.bind("<FocusIn>",on_enter4)
    entrybox4.bind("<FocusOut>",on_leave4)

    def change_password():
        user = entrybox3.get()
        new_password = entrybox4.get()
        data = []
        with open("Logindatabase.txt","r") as f:
            data = f.read().split("\n")
        if user in data:
            i = data.index(user)
            data[i+1] = new_password
        else:
            messagebox.showerror("Error","User not Found")
            return
        with open("Logindatabase.txt","w") as f:
            for i in data:
                f.write(i+"\n")
            messagebox.showinfo("Success","Password changed Successfully")

    def close():
        screen.destroy()
    btn1 = Button(screen,text = "PROCEED",width=10,height=1,bg="deeppink",fg="white",command=change_password)
    btn1.place(x=20,y=200)
    btn2 = Button(screen, text = "CANCEL",width=10, command=close)
    btn2.place(x=100,y=200)
    screen.mainloop()

window = Tk()
window.geometry("925x520+300+200")
window.title("Login Page")
window.resizable(0,0)

image1 = PhotoImage(file = "C:\\Users\\dell\\Downloads\\Sunset from see.png")
Label(window,image=image1).place(x = 0, y = 0)
Label(window,text="Welcome to my login page", background = "#5c5fc8",foreground="white",font=("Times",30,"bold italic")).place(x=300,y=20)

frame = Frame(window,width=500,height=250,bg="white")
frame.place(x = 270, y = 120)
Label(frame,text = "Login to your account",bg = "white",fg="black",font=("Times",20,"bold italic")).place(x = 100, y = 10)
label1 = Label(frame,text="Username : ",bg = "white",fg="black",font=("Times",15,"bold italic"))
label1.place(x = 10,y = 50)
entrybox1 = Entry(frame, width=45,bg="white",fg="black",font=("Times",15,"normal"),border=0)
entrybox1.place(x = 130,y = 50)
Frame(frame,width=300,height=1,bg="black").place(x=130,y=80)

def on_enter(event):
    entrybox1.delete(0,END)

def on_leave(event):
    name = entrybox1.get()
    if name == "":
        entrybox1.insert(0,"Email/Username")
entrybox1.insert(0,"Email/Username")
entrybox1.bind("<FocusIn>",on_enter)
entrybox1.bind("<FocusOut>",on_leave)

label2 = Label(frame,text="Password : ",bg = "white",fg="black",font=("Times",15,"bold italic"))
label2.place(x = 10,y = 100)
entrybox2 = Entry(frame, width=45,bg="white",fg="black",font=("Times",15,"normal"),border=0)
entrybox2.place(x = 130,y = 100)
Frame(frame,width=300,height=1,bg="black").place(x=130,y=130)

def on_enter2(event):
    entrybox2.delete(0,END)

def on_leave2(event):
    name = entrybox2.get()
    if name == "":
        entrybox2.insert(0,"Password")
entrybox2.insert(0,"Password")
entrybox2.bind("<FocusIn>",on_enter2)
entrybox2.bind("<FocusOut>",on_leave2)
entrybox2.config(show="*")

def show_password():
    if hidepassword.get() == 1:
        entrybox2.config(show="")
    elif hidepassword.get() == 0:
        entrybox2.config(show="*")

hidepassword = IntVar()

checkbox = Checkbutton(frame,text="Show Password",bg = "white",command=show_password,
                       variable=hidepassword,onvalue=1,offvalue=0)
checkbox.place(x = 100, y = 150)

button1 = Button(frame, text="Login",bg="Light grey",cursor="hand2",foreground="black",font="Arial 10 underline",
                 border=1,width=25,height=1,command=login,activebackground="dark blue",activeforeground="white")
button1.place(x=10,y=200)

button2 = Button(frame, text="Signup",bg="Light grey",cursor="hand2",foreground="black",font="Arial 10 underline",
                 border=1,width=25,height=1,command=signup,activebackground="dark blue",activeforeground="white")
button2.place(x=230,y=200)

button3 = Button(frame,text = "Forgot Password",bg="white",fg="black",cursor="Hand2",font = "Arial 10 underline",
                 border=0,width=30,command=forgot_password)
button3.place(x=120,y = 230)

window.mainloop()