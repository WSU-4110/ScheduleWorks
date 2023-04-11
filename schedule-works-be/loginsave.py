import privateInfo
import os

def login():
    if os.path.exists('privateInfo.py'):
        with open('privateInfo.py', 'r') as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()

        remember_me = input("Remember me? (y/n): ")

        if remember_me.lower() == 'y':
            with open('privateInfo.json', 'w') as f:
                f.write(f"username = '{username}'\npassword = '{password}'")
                print("Remembered login info saved.")
        else:
            print("Remembered login info not saved.")

        user_input_username = input("Username: ")
        user_input_password = input("Password: ")

        if user_input_username == username and user_input_password == password:
            print("Login successful!")
        else:
            print("Invalid username or password.")
    else:
        print("Login info not found.")

