print("Welcome to BMI Calculator")

hu = input("Enter the unit you want for height : ")
h = float(input("Enter height in cm : "))
hw = input("Enter the unit you want for weight")
w = float(input("Enter weight in kg : "))

if hu == "cm":
    hm = h/100
elif hu == "m":
    hm = h
elif

bmi = w/(hm*hm)
bmi = bmi.__round__(2)

print(f"Your BMI is : {bmi}")
if bmi <= 18.4:
    print("You are Under Weight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are in Healthy Range")
else:
    print("Yuo are Obese")