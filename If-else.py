username = input("Enter username: ")

if username == "":
    print("Please enter a username.")
    print("")
    username = input("Enter username: ")


else:
    print(f"Hello, {username}")