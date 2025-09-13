'''
Viết hàm analyze_numbers(*args) trả về:
Tổng các số,
Giá trị lớn nhất,
Giá trị nhỏ nhất.
'''
def analyze_numbers(*args):
    if not args:
        return (0, None, None)
    
    total = sum(args)
    maximum = max(args)
    minimum = min(args)
    
    return (total, maximum, minimum)

number_list = input("Entrer numbers separated by spaces: ").split()
numbers = [float(number) for number in number_list]
result = analyze_numbers(*numbers)
print(f"Sum: {result[0]}, Max: {result[1]}, Min: {result[2]}")