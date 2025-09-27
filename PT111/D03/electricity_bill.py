# Electricity bill calculator based on usage.
previous_e_index = int(input("Enter the previous electricity index (kWh): "))
current_e_index = int(input("Enter the current electricity index (kWh): "))
e_used = current_e_index - previous_e_index
print("You have used", e_used, "kWh of electricity over the last month.")
if e_used <= 50:
    level_1 = e_used * 1678 #The level 1 electricity unit price applies to the first 50 kWh.
    e_bill = level_1
elif e_used <= 100:
    level_1 = 50 * 1678
    level_2 = (e_used - 50) * 1734 #The level 2 electricity unit price applies to the next 50 kWh.
    e_bill = level_1 + level_2
else:
    level_1 = 50 * 1678
    level_2 = 50 * 1734
    level_3 = (e_used - 100) * 2014 #The Level 3 electricity unit price applies when consumption exceeds the first 100 kWh
    e_bill = level_1 + level_2 + level_3 
print("Your electricity bill is: ", e_bill, "VND.")