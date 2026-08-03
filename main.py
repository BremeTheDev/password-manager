from menu_pass import menu
from add_pass import add
from view_pass import view
from search_pass import search
from delete_pass import dlt
from master_pass import masterPass

authentication = False
if authentication is True:
    menu()
    while True:
        try:
            choice = int(input("\nChoice:"))
            if choice == 1:
                add()
            elif choice == 2:
                view()
            elif choice == 3:
                search()
            elif choice == 4:
                dlt()
            elif choice == 5:
                break
            else:
                print("| INVALID CHOICE! |")
        except ValueError:
            print("| INVALID CHOICE! |")
else:
    print("| INCORRECT PASSWORD! TRY AGAIN! |")