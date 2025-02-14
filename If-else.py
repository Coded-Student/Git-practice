username = input("Enter username: ")
password = input("Enter a password: ")

if username == "" and password == "" :
    print("Please enter a username and password.")
    print("")
    username = input("Enter username: ")
    password = input("Enter password: ")

elif username == username and not password :
    print(f"Incorrect password, please try again.")
    print("")
    password = input("Enter password: ")

else:
    print(f"Hello, {username}")