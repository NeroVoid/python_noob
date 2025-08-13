# Solve a first degree equation ax + b = 0
coefficient_a = float(input("Enter the coefficient a: "))
coefficient_b = float(input("Enter the coefficient b: "))
if coefficient_a == 0:
    if coefficient_b == 0:
        print("The equation has infinite solutions.")
    else:
        print("The equation has no solution.")
else:
    x = -coefficient_b / coefficient_a
    print("The solution is x =", x)