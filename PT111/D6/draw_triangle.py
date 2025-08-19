#This code helps in drawing a triangle
height = int(input("Enter the height of the triangle: "))
print("Select the type of triangle you want to draw \n")
type_of_triangle = int(input("1. Right-sided triangle\n"
                             "2. Inverted right-sided triangle\n"
                             "3. Left-sided triangle\n"
                             "4. Inverted left-sided triangle\n"
                             "5. Isosceles triangle\n"
                             "6. Inverted isosceles triangle\n"
                             "Enter your choice (1-6): "))
r = 0
#Drawing a right-sided triangle
if type_of_triangle==1:
    for r in range(height):
        for c in range(r+1):
            print("*", end="")
        print()
#Drawing an inverted right-sided triangle
elif type_of_triangle==2:
    for r in range(height):
        for c in range(r,height):
            print("*", end="")
        print()
#Drawing a left-sided triangle
elif type_of_triangle==3:
    for r in range(height):
        for c in range(r,height):
            print(" ", end="")
        for c in range(r+1):
            print("*", end="")
        print()
#Drawing an inverted left-sided triangle
elif type_of_triangle==4:
    for r in range(height):
        for c in range(r+1):
            print(" ", end="")
        for c in range(r,height):
            print("*", end="")
        print()
#Drawing an isosceles triangle
elif type_of_triangle==5:
    for r in range(height):
        for c in range(r,height):
            print(" ", end="")
        for c in range(r+1):
            print("*", end="")
        for c in range(r):
            print("*", end="")
        print()
#Drawing an inverted isosceles triangle
elif type_of_triangle==6:
    for r in range(height):
        for c in range(r+1):
            print(" ", end="")
        for c in range(r,height):
            print("*", end="")
        for c in range(r,height-1):
            print("*", end="")
        print()
else:
    print("Invalid choice! Please select a number between 1 and 6.")