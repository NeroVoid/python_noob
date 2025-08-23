orders = [
    ["A001", "USB Cable", 3, 4.5],
    ["A002", "Keyboard", 1, 25.0],
    ["A003", "Mouse", 2, "not_a_price"],
    ["A004", "Monitor", None, 120.0],        
    ["A005", "Laptop Stand", 2, 19.99],
]

valid_rows = 0 #Tracking successful orders
invalid_rows = 0 #Tracking invalid orders
max_order_value = 0
total_revenue = 0

for order in orders:

    if len(order) == 4:
        order_id, product_name, quantity, unit_price = order
        #Check the requirements for each component of an order
        if (
            isinstance(order_id, str) and order_id.strip() != "" and
            isinstance(product_name, str) and product_name.strip() != "" and
            isinstance(quantity, int) and quantity > 0 and
            (isinstance(unit_price, float) or isinstance(unit_price, int)) and unit_price > 0
        ):
            valid_rows += 1
            total_revenue += quantity*unit_price
            order_value = quantity * unit_price
            if order_value > max_order_value:
                max_order_value = order_value

        else:
            invalid_rows += 1
            continue
    
    else: 
        invalid_rows += 1
        continue
        
print(f"REVENUE REPORT")
print(f"Valid orders: {valid_rows} \n"
      f"Invalid orders: {invalid_rows} \n"
      f"Total revenue: {round(total_revenue, 2)} \n"
      f"Max order value: {round(max_order_value, 2)}")