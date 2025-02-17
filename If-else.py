#       Log in project

username = input("Enter username: ")
password = input("Enter a password: ")
print("")


if not username and not password :
    print("Invalid username or password")
    print("")
    username = input("Enter username: ")
    password = input("Enter password: ")

elif username == username and not password :
    print(f"Invalid password.")
    print("")
    username = input("Enter username: ")
    password = input("Enter password: ")

else:
    print("Invalid username or password")