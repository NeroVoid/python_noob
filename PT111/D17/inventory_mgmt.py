inventory = {
    "Apple": 0,
    "Banana": 100,
    "Orange": 75
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
            product_name = input("Enter product name to sell: ").title()
            if product_name not in inventory:
                print(f"{product_name} does not exist.")
                continue
            if check_out_of_stock(product_name):
                continue
            while True:
                #Ensure valid input for sales volume or return to main menu
                sales_volume = input("Enter quantity to sell (or type 'back' to return to main menu): ")
                if sales_volume.lower() in ['back', 'b']:
                    break
                try:
                    if int(sales_volume) > 0:
                        sell_product(product_name, sales_volume)
                        break
                except ValueError:
                    pass
                print("Invalid input. Enter a positive number for quantity or 'back' to return to main menu.")

        elif selection == '3':
            product_name = input("Enter product name to add: ").title()

            if product_name in inventory:
                print(f"{product_name} already exists in inventory. Current stock: {inventory[product_name]} units.")
                print("Do you want to update the stock instead? (yes/no)")
                if input().lower() in ['yes', 'y']:
                    add_stock(product_name)
                else:
                    print("No changes made to inventory.")
            
            else:
                while True:
                    initial_quantity = input("Enter initial stock quantity (or type 'back' to return to main menu): ")
                    if initial_quantity.lower() in ['back', 'b']:
                        break
                    try:
                        if int(initial_quantity) >= 0:
                            add_product(product_name, initial_quantity)
                            break
                    except ValueError:
                        pass
                    print("Invalid input. Enter a positive number for quantity or 'back' to return to main menu.")
        
        elif selection == '4':
            remove_out_of_stock()   
        
        elif selection == '5':
            product_with_highest_stock()
        
        elif selection == '6':
            print("Exiting Inventory Management System.")
            break
        
        else:
            print("Invalid selection. Please choose a valid option (1-6).")

#Displays the entire list of products in the inventory along with their in-stock quantity.

def display_inventory():
    print("--- Current Inventory ---")
    if not inventory:
        print("Inventory is empty.")
        return
    else:
        for product_name, current_quantity in sorted(inventory.items()):
            print(f"{product_name}: {current_quantity} units")

#Check whether a product is out of stock and displaying a message if it is.

def check_out_of_stock(product_name):
    if inventory.get(product_name, 0) == 0:
        print(f"{product_name} is out of stock.")
        return True
    return False

#Sells a specified quantity of a product and updating the inventory accordingly.

def sell_product(product_name, sales_volume):
    sales_volume = int(sales_volume)
    if product_name in inventory:
        if sales_volume <= inventory[product_name]:
            inventory[product_name] -= sales_volume
            print(f"Sold {sales_volume} units of {product_name}. Remaining stock: {inventory[product_name]} units.")
        else:
            print(f"Insufficient stock for {product_name}. Available: {inventory[product_name]} units.")

#Adds a new product to the inventory with an initial stock quantity.

def add_product(product_name, initial_quantity):
    initial_quantity = int(initial_quantity)
    if product_name not in inventory:
        if initial_quantity >= 0:
            inventory[product_name] = initial_quantity
            print(f"Added {product_name} with {initial_quantity} units to the inventory.")
        else:
            print("Initial quantity must be a positive number.")

#Adds stock to an existing product.

def add_stock(product_name):
    if product_name in inventory:
        while True:
            added_quantity = input(f"Enter quantity to add to {product_name} (or type 'back' to return to main menu): ")
            if added_quantity.lower() in ['back', 'b']:
                break
            try:
                if int(added_quantity) > 0:
                    inventory[product_name] += int(added_quantity)
                    print(f"Added {added_quantity} unit to {product_name}. New stock: {inventory[product_name]} units.")
                    break
            except ValueError:
                pass
            print("Invalid input. Please enter a positive number for quantity of 'back' to return to main menu.") 

#Removes all products that are out of stock from the inventory.

def remove_out_of_stock():
    out_of_stock = [product for product, quantity in inventory.items() if quantity == 0]

    if out_of_stock:
        for product in out_of_stock:
            del inventory[product]
        print(f"Removed out-of-stock products: {', '.join(out_of_stock)}")
    else:
        print("No out-of-stock products to remove.")

#Identifies and displays the product with the highest stock quantity.

def product_with_highest_stock():
    if not inventory:
        print("Inventory is empty.")
        return

    max_quantity = max(inventory.values())

    if max_quantity == 0:
        print("All products are out of stock.")
        return
    else:
        top_products = [product_name for product_name, current_quantity in inventory.items() if current_quantity == max_quantity]
        
        if len(top_products) > 1:
            print(f"Products with highest stock: {', '.join(top_products)} ({max_quantity} units each)")
        else:
            print(f"Product with highest stock: {top_products[0]} ({max_quantity} units)")

if __name__ == "__main__":
    inventory_management()