# This script helps calculate the taxi fare based on distance traveled.
print("Welcome to the Taxi Fare Calculator! \n"
    "Fare card: \n"
    "1. Base fare: 20,000 VND for the first 1km \n" 
    "2. For 2 to 5 km: 15,000 VND/km after the first km \n" 
    "3. For 6 to 10 km: 13,000 VND/km after the fifth km \n" 
    "4. For more than 10 km: 10,000 VND/km for every km after the tenth km")

print("PROMOTION: 10% discount if your total payment is greater than 200,000 VND.")

distance = int(input("Enter the distance you traveled in km: "))

if distance <=1:
    fare = 20000 # Base fare for up to 1 km
elif distance <= 5:
    fare = 20000 + (distance - 1) * 15000 # Fare for 2 to 5 km
elif distance <= 10:
    fare = 20000 + 4 * 15000 + (distance - 5) * 13000 # Fare for 6 to 10 km
elif distance > 10:
    fare = 20000 + 4 * 15000 + 5 * 13000 + (distance - 10) * 10000 # Fare for more than 10 km
print("The total taxi fare for", distance, "km is:", round(fare), "VND.")

if fare > 200000:
    print("You have received 10% off, equivalent to:", round(fare * 0.1), "VND")
    fare = round(fare * 0.9) # Apply 10% discount

print("The amount to be paid is:", fare, "VND.")