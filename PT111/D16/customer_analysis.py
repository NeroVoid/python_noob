A = {"Nam", "Hoa", "Linh", "Minh"}
B = {"Hoa", "Tuan", "Nam", "An"}

print("Common customers of both stores: ")
common_customers = sorted(A & B)
for idx, customer in enumerate(common_customers, 1):
    print(f"{idx}. {customer}")
if common_customers:
    print()

print("Customers only in store A: ")
storeA_customers = sorted(A - B)
for idx, customer in enumerate(storeA_customers, 1):
    print(f"{idx}. {customer}")
if storeA_customers:
    print()

print("Customers only in store B: ")
storeB_customers = sorted(B - A)
for idx, customer in enumerate(storeB_customers, 1):
    print(f"{idx}. {customer}")
if storeB_customers:
    print()

print("All customers (no duplicates): ")
all_customers = sorted(A | B)
for idx, customer in enumerate(all_customers, 1):
    print(f"{idx}. {customer}")
print(f"Total number of unique customers: {len(all_customers)} \n")