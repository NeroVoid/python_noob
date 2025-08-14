# This code helps convert USD to VND and vice versa.
print("Please select the conversion type:\n"
      "1. USD to VND\n"
      "2. VND to USD")
conversion_type = input("Enter 1 or 2: ")
if conversion_type == '1':
    usd_amount = float(input("Enter the amount in USD: "))
    vnd_amount = round(usd_amount * 26000)  # Assuming 1 USD = 26000 VND
    print(usd_amount, "USD is equal to", vnd_amount, "VND.")
elif conversion_type == '2':
    vnd_amount = round(float(input("Enter the amount in VND: ")))
    usd_amount = vnd_amount / 26000  # Assuming 1 USD = 26000 VND
    print(vnd_amount,"VND is equal to", usd_amount,"USD.")
else:
    print("Invalid selection. Please enter 1 or 2.")