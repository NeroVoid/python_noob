def rectangle_area(length,width):
    area = round(length*width,2)
    print(f"The area of ​​a rectangle with length {length} and width {width} is {area}.")
    return rectangle_area

length = float(input("Enter the rectangle length: "))
width = float(input("Enter the rectangle width: "))
rectangle_area(length,width)