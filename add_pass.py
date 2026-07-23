import json
def add():
    website = input("Website:")
    username = input("Username:")
    password = input("Password:")
    with open("passwords.json","r") as file:
        data = json.load(file)
    data[website] = {
        "username" : username,
        "password" : password
    }
    with open("passwords.json","w") as file:
        json.dump(data, file, indent=4)
    print("Password Successfully Entered!")