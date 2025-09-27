# This code calculates the Body Mass Index (BMI) based on user input for weight and height.
# Enter the height and weight values in appropriate units and values.
weight = float(input("Enter your weight in kilograms: "))
if weight <= 0:
    print("Weight must be a positive number.")
elif 0 < weight < 30 or weight > 300:
    print("Please enter realistic values for the weight.")
else:
    height = float(input("Enter your height in meters: "))
    if height <= 0:
        print("Height must be a positive number.")
    elif 0 < height < 0.3 or height > 3.0:
        print("Please enter realistic values for the height.")
    else:
        # Calculate BMI
            bmi = round((weight / (height ** 2)), 1)
            print("Your BMI is: ", bmi)

            # Assessing an individual's health based on BMI categories.
            match bmi:
                case _ if bmi < 18.5:
                    print("You are underweight.")
                case _ if 18.5 <= bmi < 24.9:
                    print("You have a normal weight.")
                case _ if 25 <= bmi < 29.9:
                    print("You are overweight.")
                case _:
                    print("You are obese.")