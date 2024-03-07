from tkinter import*
from tkinter import filedialog
import os
from tkinter import messagebox

def new_file():
	global file
	window.title("Untitled.txt")
	file = None
	textArea.delete(1.0,END)

def open_file():
	file = filedialog.askopenfilename(defaultextension = ".txt",filetypes = [("All Files ","*.*"),("Text Documents","*.txt")])
	if file == "":
		file = None
	else:
		window.title(os.path.basename(file))
		textArea.delete(1.0,END)
	f = open(file,"r")
	textArea.insert(1.0,f.read())
	f.close

def save_file():
	file = filedialog.asksaveasfilename(initialfile = "Untitled.txt",defaultextension = ".txt",
										filetypes = [("All Files","*.*"),("Text Documents","*.txt")])
	if file == "":
		file = None

	else:
		f = open(file,"w")
		f.write(textArea.get(1.0,END))
		f.close()
		window.title(os.path.basename(file))
		messagebox.showinfo("Message","File saved successfully")

def close_file():
	window.destroy()

def cut():
	textArea.event_generate("<<Cut>>")

def copy():
	textArea.event_generate("<<Copy>>")

def paste():
	textArea.event_generate("<<Paste>>")

def light_mode():
	textArea.config(background = "white", foreground = "black", insertbackground = "black")

def dark_mode():
	textArea.config(background = "black", foreground = "white", insertbackground = "white")

window = Tk()
window.title("Rich Text Editor")
window.geometry("500x500")

textArea = Text(window, font = ("Bahnschrift",20,"normal"))
textArea.pack(expand = True,fill = BOTH)

Menubar = Menu(window, tearoff = 0)

FileMenu = Menu(Menubar, tearoff = 0)
FileMenu.add_command(label = "New", command = new_file)
FileMenu.add_command(label = "Open", command = open_file)
FileMenu.add_command(label = "Save", command = save_file)
FileMenu.add_command(label = "Close", command = close_file)

Menubar.add_cascade(label = "File", menu = FileMenu)

EditMenu = Menu(Menubar,tearoff = 0)
EditMenu.add_command(label = "Cut", command = cut)
EditMenu.add_command(label = "Copy", command = copy)
EditMenu.add_command(label = "Paste", command = paste)
Menubar.add_cascade(label = "Edit", menu = EditMenu)

ModeMenu = Menu(Menubar, tearoff = 0)
ModeMenu.add_command(label = "Dark", command = dark_mode)
ModeMenu.add_command(label = "Light", command = light_mode)
Menubar.add_cascade(label = "Theme", menu = ModeMenu)

scrollbar = Scrollbar(textArea)
scrollbar.pack(side = RIGHT, fill = Y)
textArea.config(yscrollcommand = scrollbar.set)

window.bind("<Control-s>",lambda event : save_file())
window.config(menu = Menubar)
window.mainloop()