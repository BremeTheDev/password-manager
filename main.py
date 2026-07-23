from menu_pass import menu
from add_pass import add
from view_pass import view
from search_pass import search

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
            break
        else:
            print("INVALID CHOICE!")
            continue
    except ValueError:
        print("INVALID CHOICE!")