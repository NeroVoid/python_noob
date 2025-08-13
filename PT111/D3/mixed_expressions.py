# This scripts calculates mixed expressions
number_a = int(input("Enter the value of interger a: "))
number_b = int(input("Enter the value of interger b: "))
number_c = int(input("Enter the value of interger c: "))
result = (number_a + number_b) * number_c - number_a ** 2 // (number_b + 1)
print ("The result of the expression is:", result)