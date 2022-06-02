import os


class Menu:
    def __init__(self):
        pass

    def display_menu(self, menu_list):
        # clearConsole()
        for id, item in enumerate(menu_list):
            print(f"{id+1:^4}{item:40}")
        print()
        while True:

            try:
                choice = int(input("choisissez un indice : "))
            except ValueError:
                print("vous devez entrer un entier")
            else:
                if 1 <= choice <= len(menu_list):
                    break
                else:
                    print("vous devez entrer un entier entre 1 et", len(menu_list))
        return choice


clearConsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")
