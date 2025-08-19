number = int(input("Enter an integer greater than 10: "))

while number <= 10:
    print("The number you entered is invalid. Please try again. \n")
    number = int(input("Enter an integer greater than 10: "))

print("You entered successfully:", number)