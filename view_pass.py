import json
def view():
    with open("passwords.json","r") as file:
        data_read = json.load(file)
        print(data_read)