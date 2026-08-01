import json
from cryptography.fernet import Fernet
def add():
    website = input("\nWebsite:")
    username = input("Username:")
    password = input("Password:")

    key = Fernet.generate_key()
    with open("key.key","wb") as file:
        file.write(key)
    with open("key.key","rb") as file:
        file.read()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode()).decode()

    with open("passwords.json","r") as file:
        data = json.load(file)
    if website in data:
        print("| PASSWORD ALREADY EXISTS! |")
    else:
        data[website] = {
            username : encrypted_password
        }
        with open("passwords.json","w") as file:
            json.dump(data, file, indent=4)
        print("\n|| PASSWORD SUCCESSFULLY ENTERED! ||")