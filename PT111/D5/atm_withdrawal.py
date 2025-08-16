# This script simulates an ATM withdrawal process.
balance = 5000000 # Initial balance in the ATM account.
withdrawal_amount = int(input("Enter the amount you want to withdraw (VND): "))
if withdrawal_amount % 50000 ==0: # Check if the withdrawal amount is a multiple of 50,000 VND.
    if withdrawal_amount <= balance: # Check if there are sufficient funds.
        balance = balance - withdrawal_amount
        print("Withdrawal successful! Your new balance is: ", balance, "VND")
    else:
        print("Insufficient funds for this withdrawal.")
else:
    print("The amount must be a multiple of 50,000 VND.")