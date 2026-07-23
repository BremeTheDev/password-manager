from menu_pass import menu
from add_pass import add
from view_pass import view
from search_pass import search

choice = menu()
if choice == 1:
    add()
elif choice == 2:
    view()
elif choice == 3:
    search()
elif choice == 4:
    pass    
else:
    print("Invalid Option!")