def print_fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

if __name__ == "__main__":
    num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
    print_fibonacci_sequence(num_terms)