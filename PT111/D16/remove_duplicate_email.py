emails = ["a@gmail.com", "b@yahoo.com", "a@gmail.com", "c@gmail.com", "b@yahoo.com"]
unique_emails = sorted(set(emails))
print("Email list: ")
for email in unique_emails:
    print(f"- {email}")