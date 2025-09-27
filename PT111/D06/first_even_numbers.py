even_number_count = int(input("Enter the number of even numbers to print: "))
if even_number_count==1:
    print("The first even number is: 2")
elif even_number_count > 1:
    print("The first", even_number_count, "even numbers are:")
    even_number_list= []
    number = 0
    for number in range(1, even_number_count* 2 + 1):
        if number % 2 == 0:
            even_number_list.append(number)
            number += 1
        else:
            continue
    print(even_number_list)
else:
    print("Please enter a positive integer greater than 0.")