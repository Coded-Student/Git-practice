import sys


def log_in(input_username, input_password):
    # Check if username or password is empty
    if not input_username or not input_password:
        print("Invalid username or password.")
    # Check if the username is correct and password is incorrect
    elif input_username == "nzhao" and input_password != "roki12":
        print("Invalid password.")
    # Check if both username and password are correct
    elif input_username == "nzhao" and input_password == "roki12":
        print("You successfully logged in.")
        return True  # Successful login
    else:
        print("Invalid username or password.")
    return False  # Failed login


# Main program
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Please enter username: ")
    password = input("Please enter device id: ")

    if log_in(username, password):
        break  # Exit loop if login is successful.
    attempts += 1

    if attempts == max_attempts:
        print("Too many failed attempts. Exiting program.")
        sys.exit()  # Exit the program if the attempts exceed limit.
