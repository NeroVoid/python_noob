#This code helps manage vouchers by generating unique codes, checking their validity, and allowing user interaction to verify a voucher code.
import random
import string
from datetime import date, timedelta, datetime
from coupon_utils import generate_code, create_coupons, is_valid

def main():
    # Create a list of coupons
    num_coupons = 10
    discount = 10  # Percentage discount
    days_valid = 7
    coupons = create_coupons(num_coupons, discount, days_valid)
    
    # Print the list of coupons
    print("Generated Coupons:")
    for code, disc, expiry in coupons:
        print(f"CODE={code} | Discount={disc}% | Expires={expiry}")
    
    # Get user input for a coupon code to check
    user_code = input("\nEnter a coupon code to check: ").strip().upper()
    
    # Check if the entered code exists and is valid
    now = date.today()
    found = False
    
    for code, disc, expiry in coupons:
        if code == user_code:
            found = True
            valid_status = "VALID" if is_valid(expiry, now) else "EXPIRED"
            print(f"CODE={code} | Discount={disc}% | Expires={expiry} | Status={valid_status}")
            break
    
    if not found:
        print("Coupon code not found.")

if __name__ == "__main__":
    
    main()  # Run the main function if this script is executed directly
    