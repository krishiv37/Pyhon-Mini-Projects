from tkinter import *
import random

HEIGHT = 700
WIDTH = 700
SNAKECOLOUR = "#FFCC00"
FOODCOLOUR = "Red"
SPEED = 125

class Snake:
    def __init__(s):
        s.body_size = 3
        s.coordinates = []
        s.squares = []
        for i in range(3):
            s.coordinates.append([0,0])
        for x,y in s.coordinates :
            square = canvas.create_rectangle(x,y,x+50,y+50,fill= SNAKECOLOUR, tag = "snake")
            s.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0,WIDTH/50 - 2) * 50
        y = random.randint(0,HEIGHT/50 - 2) * 50
        self.coordinates = [x,y]
        canvas.create_oval(x,y,x+50,y+50,fill = FOODCOLOUR,tag = "food")

def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if new_direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if new_direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if new_direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if new_direction != "up":
            direction = new_direction

def detect_collissions():
    x = snake.coordinates[0][0]         # Snake Head x
    y = snake.coordinates[0][1]         # Snake Head y
    if x < 0 or x > WIDTH:             # Vertical Borders
        return True
    elif y < 0 or y > HEIGHT:          # Horizontal Borders
        return True
    for parts in snake.coordinates[1:]:
        if x == parts[0] and y == parts[1]:
            return True
    return False

def gameover():
    canvas.delete(ALL)
    canvas.create_text(350,350,text="Game Over",fill = "red",font=("Chiller",30,"bold"),tag = "gameover")

def game(snake,food):
    """x = snake.coordinates[0,0]
    y = snake.coordinates[0,1]"""
    x,y = snake.coordinates[0]
    if direction == "left":
        x = x - 50
    elif direction == "right":
        x = x + 50
    elif direction == "up":
        y = y - 50
    elif direction =="down":
        y = y + 50
    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x,y,x+50,y+50,fill= SNAKECOLOUR)
    snake.squares.insert(0,square)
    if x == food .coordinates[0] and y == food.coordinates[1]:
        global score
        score += 10
        label.config(text= f"Score = {score}",font = ("Arial",30,"bold"))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if detect_collissions():
        gameover()
    else:
        window.after(SPEED,game,snake,food)


############################ USER INTERFACE ############################

window = Tk()
window.title("Snake Game")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(0,0)

score = 0

label = Label(text = f"Score = {score}",font = ("Ariel",30,"bold"))
label.pack()

canvas = Canvas(window, bg = "black", width=WIDTH, height=HEIGHT)
canvas.pack()

window.update()
direction = "right"
food = Food()
snake = Snake()
game(snake,food)
window.bind("<Left>",lambda event:change_direction("left"))
window.bind("<Right>",lambda event:change_direction("right"))
window.bind("<Up>",lambda event:change_direction("up"))
window.bind("<Down>",lambda event:change_direction("down"))

window.mainloop()