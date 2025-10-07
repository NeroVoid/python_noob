def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

while True:
    try:
        n = int(input("Input a positive integer: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

result = sum_numbers(n)
print(f"The sum of numbers from 1 to {n} is: {result}")