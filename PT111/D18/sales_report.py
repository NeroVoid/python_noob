import csv

# Read sales data
sales_data = []
with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert quantity and price to integers
        row["quantity"] = int(row["quantity"])
        row["price"] = int(row["price"])
        sales_data.append(row)

# Calculate revenue per product
revenue_by_product = {}
for sale in sales_data:
    product = sale["product"]
    revenue = sale["quantity"] * sale["price"]
    revenue_by_product[product] = revenue_by_product.get(product, 0) + revenue

# Print report
print("--- Sales Report ---")
for product, revenue in revenue_by_product.items():
    print(f"{product}: ${revenue}")

# Write report to CSV file
with open("sales_report.csv", "w", newline="") as report_file:
    writer = csv.writer(report_file)
    writer.writerow(["Product", "Revenue"])
    for product, revenue in revenue_by_product.items():
        writer.writerow([product, revenue])