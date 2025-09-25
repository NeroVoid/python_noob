# Print a formatted receipt for a list of products
products = [
    ["Apple", 2, 5000],
    ["Milk", 1, 12000],
    ["Bread", 3, 7000]
]

def print_receipt(products):
    print("*** SHOP XYZ RECEIPT ***")
    print("Name\tQty\tPrice")
    
    total = 0
    for name, qty, price in products:
        print(f"{name}\t{qty}\t{price}")
        total += qty * price
    
    print(f"Total:\t{total}")

print_receipt(products)