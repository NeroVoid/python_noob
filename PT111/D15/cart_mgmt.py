cart = []

def add_item():
    while True:
        item = input("Enter the item to add: ")
        if item:
            cart.append(item)
            print(f"{item} has been added to your cart. \n")
        else:
            print("Item cannot be empty.\n")
            
        continue_add = input("Do you want to add more items? (yes/no): ")
        if continue_add.lower() not in ('yes', 'y'):
            break

def remove_item():
    while True:
        if not cart:
            print("Your cart is empty, nothing to remove.\n")
            break
            
        item = input("Enter the item to remove: ")

        try:
            cart.remove(item)
            print(f"{item} has been removed from your cart.\n")
        except ValueError:
            print(f"{item} is not in your cart.\n")
            
        continue_remove = input("Do you want to remove more items? (yes/no): ")
        if continue_remove.lower() not in ('yes', 'y'):
            break

def main():
    while True:
        print("\nMenu: \n"
              "1. Add item to cart\n"
              "2. Remove item from cart\n"
              "3. View cart\n"
              "4. Exit")
        
        selection = input("Please select an option from 1 to 4: ")
        
        if selection == '1':
            add_item()

        elif selection == '2':
            remove_item()
                
        elif selection == '3':
            if cart:
                print("Items in your cart: \n")
                for (i, item) in enumerate(cart, start=1):
                    print(i, item.title())
            else:
                print("Your cart is empty.")
                
        elif selection == '4':
            print(f"Total number of items in your cart: {len(cart)}")
            print("Exit.")
            break
            
        else:
            print("Invalid selection, please select again.")

if __name__ == "__main__":
    main()