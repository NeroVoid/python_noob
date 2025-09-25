inventory = {
    "apple": 0,
    "banana": 100,
    "orange": 75
}

# Warehouse Inventory Management System
def inventory_management():
    while True:
        print("\nInventory Management System \n"
        "1. Display Inventory \n"
        "2. Sell Product \n"
        "3. Add Product \n"
        "4. Remove Out-of-Stock Products \n"
        "5. Product with Highest Stock \n"
        "6. Exit"
        )
        
        selection = input("Select a task (1-6): ")
        
        if selection == '1':
            display_inventory()

        elif selection == '2':
            product = input("Enter product name to sell: ").strip().lower()
            if check_product_exists(product):
                quantity = int(input("Enter quantity to sell: "))
                if quantity > 0:
                    sell_product(product, quantity)
                else:
                    print("Quantity must be greater than zero.")
            else:
                print(f"{product} does not exist in inventory.")

        elif selection == '3':
            product = input("Enter product name to add: ").strip().lower()
            if check_product_exists(product):
                quantity = int(input("Enter quantity to add: "))
                if quantity > 0:
                    add_product(product, quantity)
                else:
                    print("Quantity must be greater than zero.")
            else:
                print(f"{product} does not exist in inventory.")
            
        elif selection == '4':
            remove_out_of_stock()

        elif selection == '5':
            product_with_highest_stock()

        elif selection == '6':
            print("Exiting Inventory Management System.")
            break

        else:
            print("Invalid selection. Please try again.")

#Displays the entire list of products in stock along with the stock quantity of each type.
def display_inventory():
    print("Current Inventory:")
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")

#Check if the product exists in inventory
def check_product_exists(product):
    try:
        if product not in inventory:
            raise KeyError(f"{product} not found in inventory.")
    except KeyError:
        return False
    return product in inventory

#Update inventory quantity when a product is sold.
def sell_product(product, quantity):
    try:
        if inventory[product] >= quantity:
            inventory[product] -= quantity
            print(f"Sold {quantity} of {product}. New quantity: {inventory[product]}")
        else:
            print(f"Not enough {product} in stock to sell {quantity}. Current stock: {inventory[product]}")
    except KeyError:
        print(f"{product} not found in inventory.")

#Add new product(s) to the inventory
def add_product(product, quantity):
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity
    print(f"Added {quantity} of {product}. New quantity: {inventory[product]}")

#Remove out-of-stock products from the inventory
def remove_out_of_stock():
    out_of_stock = [product for product, quantity in inventory.items() if quantity == 0]
    for product in out_of_stock:
        del inventory[product]
        print(f"Removed {product} from inventory as it is out of stock.")

#Find the product with the highest stock quantity
def product_with_highest_stock():
    if not inventory:
        print("Inventory is empty.")
        return
    max_product = max(inventory, key=inventory.get)
    print(f"Product with the highest stock: {max_product} ({inventory[max_product]})")

if __name__ == "__main__":
    inventory_management()