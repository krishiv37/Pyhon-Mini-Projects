import random

print("Welcome to our Rock - Paper - Scissors app")
inp = str(input("Choose any one rock or paper or scissors : "))

option = ["rock","paper","scissors"]

while inp not in option:
    print("You Selcted Wrong Input")
    exit()

ran = random.choice(option)

print(f"You Choose : {inp}")
print(f"Computer Choose : {ran}")

if inp == ran:
    print("It is a Tie")
elif inp == "scissors" and ran == "paper":
    print("You Win")
elif inp == "rock" and ran == "scissors":
    print("You Win")
elif inp == "paper" and ran == "rock":
    print("You Win")
else:
    print("You Lose")