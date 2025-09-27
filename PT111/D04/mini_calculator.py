#This is a simple calculator that can perform addition, subtraction, multiplication, and division.
first_number = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
second_number = float(input("Enter the second number: "))
if operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/' and second_number != 0:
    result = first_number / second_number
else:
    result = "Invalid operation."
print(first_number, operation, second_number, "=", result) 