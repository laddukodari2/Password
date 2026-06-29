password = input("Enter your password: ")

if len(password) < 8:
    print("Weak Password")
elif password.isalpha():
    print("Password should contain numbers.")
elif password.isdigit():
    print("Password should contain letters.")
else:
    print("Strong Password")