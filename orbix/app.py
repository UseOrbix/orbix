import json
import os

DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        # Initialize default user if not present
        with open(DATA_FILE, 'w') as f:
            json.dump({"username": "user", "password": "0000"}, f, indent=4)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def login(data):
    print("=== Login ===")
    uname = input("Username: ")
    pwd = input("Password: ")
    if uname == data["username"] and pwd == data["password"]:
        print("Login successful!")
        return True
    else:
        print("Login failed! Incorrect username or password.")
        return False

def change_details(data):
    print("=== Change Account Details ===")
    new_uname = input("New username (leave blank to keep current): ")
    new_pwd = input("New password (leave blank to keep current): ")
    if new_uname:
        data["username"] = new_uname
    if new_pwd:
        data["password"] = new_pwd
    save_data(data)
    print("Account details updated.")

def main():
    data = load_data()
    while True:
        if login(data):
            print("Welcome,", data["username"])
            choice = input("Do you want to change account details? (y/n): ")
            if choice.lower() == 'y':
                change_details(data)
            break
        else:
            retry = input("Try again? (y/n): ")
            if retry.lower() != 'y':
                break

if __name__ == '__main__':
    main()
