#This is a module for generating and managing coupon codes with expiration dates.
import random
import string
from datetime import datetime

def generate_code(length=8):
    # Generate a random coupon code consisting of uppercase letters and digits
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_coupons(n, discount, days_valid):
    from datetime import date, timedelta
    coupons = []
    today = date.today()
    expiry_date = today + timedelta(days=days_valid)
    expiry_date_str = expiry_date.strftime("%Y-%m-%d")
    
    existing_codes = set()
    
    for _ in range(n):
        code = generate_code()
        while code in existing_codes:  # Ensure unique codes
            code = generate_code()
        existing_codes.add(code)
        coupons.append([code, discount, expiry_date_str])
    
    return coupons

def is_valid(expiry_date_str, now):
    # Check if the coupon is still valid based on the current date
    expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d").date()
    return now <= expiry_date_str