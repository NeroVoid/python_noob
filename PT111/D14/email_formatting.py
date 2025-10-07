email = input("Enter email: ").strip().lower()

if "@" in email and "." in email.split("@")[-1]:
    print("Valid email")
else:
    print("Invalid email. Please enter a valid email address.")