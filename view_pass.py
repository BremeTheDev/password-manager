import json
def view():
    with open("passwords.json","r") as file:
        data_read = json.load(file)
        print("\n-----------------")
        print("| ALL PASSWORDS |")
        print("-----------------")
        for website, data in data_read.items():
            for username, password in data.items():
                print("\nWebsite:", website)
                print("Username:", username)
                print("Password:", password)