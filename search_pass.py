import json
def search():
    with open("passwords.json","r") as file:
        data_read = json.load(file)
    while True:        
        website = input("\nWebsite:")
        if website in data_read:
            account = data_read[website]
            print("\n------------------")
            print("| FOUND PASSWORD |")
            print("------------------")
            for username, password in account.items():
                print("Website:", website)
                print("Username:", username)
                print("Password:", password)
            break
        else:
            print("| PASSWORD NOT FOUND! |")
            continue