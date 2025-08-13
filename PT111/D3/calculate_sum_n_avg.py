# This code calculates the sum and the average of three numbers input by the user.
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
number_3 = float(input("Enter the third number: "))
sum = round (number_1 + number_2 + number_3,3)
average = round (sum / 3,3)
print ("The sum is:", sum)
print("The average is:", average)