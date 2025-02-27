email=input("Enter your email: ")
domain = email.split('@')[-1]
print("Extracted domain:",domain)