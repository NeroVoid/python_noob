#This script manages a shopping cart, allowing users to view products and their prices, and calculate the total cost of the cart.
cart =[
    {'name': "Laptop", 'price': 1500},
    {'name': "Mouse", 'price': 20},
    {'name': "Keyboard", 'price': 45}]

# Displaying products in the cart
print("Products in the cart:")
for item in cart:
    print("Product:", item['name'],"\n"
          "Price: $", item['price'])

# Calculating the total cost of the cart
total_cost = 0
for item in cart:
    total_cost += item['price']
print("Total cost of the cart: $", total_cost)   