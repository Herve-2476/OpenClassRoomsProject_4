import os
from views.views import Views


class Menu(Views):
    def __init__(self, menu_list):
        self.menu_list = menu_list

    def display_menu(self):
        print()
        for id, item in enumerate(self.menu_list):
            print(f"{id+1:^4}{item:40}")
        print()
        while True:

            try:
                choice = int(input("choisissez un indice : "))
            except ValueError:
                print("vous devez entrer un entier")
            else:
                if 1 <= choice <= len(self.menu_list):
                    break
                else:
                    print("vous devez entrer un entier entre 1 et", len(self.menu_list))
        return choice
