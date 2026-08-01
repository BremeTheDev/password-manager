import json
from cryptography.fernet import Fernet
def view():
    with open("passwords.json","r") as file:
        data_read = json.load(file)
        print("\n-----------------")
        print("| ALL PASSWORDS |")
        print("-----------------")
        with open("key.key","rb") as file:
            key = file.read()
        fernet = Fernet(key)
        for website, data in data_read.items():
            for username, password in data.items():
                decrypted_password = fernet.decrypt(password.encode()).decode()
                print("\nWebsite:", website)
                print("Username:", username)
                print("Password:", decrypted_password)