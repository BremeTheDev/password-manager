from cryptography.fernet import Fernet
import json

def masterPass():
    with open("config.json","rb") as file:
        config = json.load(file)

    if config["first_time_setup"] is True:
        print("\n| FIRST TIME SETUP DETECTED! |")
        print("1. Password should be atleast 12 characters long.")
        print("2. Password should contain a combination of lowercase, uppercase, special characters and digits")
        print("   with a minimum of 3 characters from each.")

        while True:
            master_password = input("\nEnter a strong master password:")

            digits = 0
            lowercase = 0
            uppercase = 0
            special_char = 0
            if len(master_password)>12:
                for character in master_password:
                    if character.isdigit():
                        digits+= 1
                    if character.isalpha():
                        if character.islower():
                            lowercase+= 1
                        else:
                            uppercase+= 1
                    else:
                        special_char+= 1


                if digits>=3:
                    if lowercase>=3:
                        if uppercase>=3:
                            if special_char>=3:

                                key = Fernet.generate_key()
                                with open("master.key","wb") as file:
                                    file.write(key)
                                fernet = Fernet(key)
                                encrypted_master_password = fernet.encrypt(master_password.encode())
                                with open("master_pass.bin","wb") as file:
                                    file.write(encrypted_master_password)
                                config["first_time_setup"] = False
                                with open("config.json","w") as file:
                                    json.dump(config, file, indent=4)
                                print("| MASTER PASSWORD SUCCESSFULLY CREATED |")
                                return True
                                break

                            else:
                                print("| NOT ENOUGH SPECIAL CHARACTERS! |")
                                continue
                        else:
                            print("| NOT ENOUGH UPPERCASE CHARACTERS! |")
                            continue
                    else:
                        print("| NOT ENOUGH LOWERCASE CHARACTERS! |")
                        continue
                else:
                    print("| NOT ENOUGH DIGITS! |")
                    continue
            else:
                print("| PASSWORD LENGTH TOO SHORT! |")
                continue

    else:        
        master_password = input("\nEnter the master password to access the vault:")
        with open("master_pass.bin","rb") as file:
            encrypted_master_password = file.read()
        with open("master.key","rb") as file:
            key = file.read()
        fernet = Fernet(key)
        decrypted_master_password = fernet.decrypt(encrypted_master_password).decode()
        if decrypted_master_password == master_password:
            return True
        else:
            return False