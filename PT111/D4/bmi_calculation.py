# This code calculates the Body Mass Index (BMI) based on user input for weight and height.
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = round((weight / (height ** 2,2))
print("Your BMI is: ", bmi)
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.") 