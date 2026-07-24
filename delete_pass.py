import json
def dlt():
    while True:
        website = input("\nWebsite:")
        with open("passwords.json", "r") as file:
            data = json.load(file)
        if website in data:
            del data[website]
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent = 4)
            print("|| PASSWORD SUCCESSFULLY DELETED! ||")
            break
        else:
            print("| PASSWORD NOT FOUND! |")
            continue