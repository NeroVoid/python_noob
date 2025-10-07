import math
import random
import datetime
print("All modules imported successfully.")

print("\n--- Math Module Examples --- \n")
n = int(input("Enter an integer (n): "))

print("Square root of n:", math.sqrt(n))
print("n squared:", math.pow(n, 2))
print("Factorial of n:", math.factorial(n))
print(f"Pi value: {math.pi}")

print("\n--- Random Module Examples --- \n")
print(f"A random integer between 1 and 100: {random.randint(1, 100)}")

fruits = ["Apple", "Banana", "Orange", "Watermelon"]
print(f"Randomly selected fruit: {random.choice(fruits)}")

print("\n--- Datetime Module Examples --- \n")
now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"Formatted date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")