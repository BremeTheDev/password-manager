import json
def search():
    with open("passwords.json","r") as file:
        data_read = json.load(file)
    website = input("Website:")
    if website in data_read:
        for username, password in website.items():
            print("Website:", website)
            print("Username:", username)
            print("Password:", password)
    else:
        print("Website not found!")