import os


class Views:
    clean_system_command = "cls" if os.name in ("nt", "dos") else "clear"

    def __init__(self, view_name):
        self.view_name = view_name

    def clear_console(self, tournament_name=""):
        os.system(self.clean_system_command)
        print("############ CHESS PROGRAM ############")
        print()
        if tournament_name:
            print("Tournoi sélectionné :", tournament_name)
            print()

    def display_line(self, line):
        form = self.format_line_display
        print(form.format(*[str(arg) for arg in line]))

    def display_db_list(self, db_table_list, id=True, order=""):
        self.clear_console()
        print(self.title_display, order)
        print()
        id_name = ""
        if id:
            id_name = "ID"

        if db_table_list:

            self.display_line([id_name] + list(self.columns_name_dict.values()))
            print()
            if id_name:
                for record in db_table_list:
                    self.display_line(
                        [record.doc_id] + [value for value in record.values()]
                    )
            else:

                for record in db_table_list:
                    self.display_line([""] + [value for value in record.values()])
            print()

    def id_choice(self, id_list, title="Choix d'un élément de la table"):
        if title:
            print(title)
            print()
        while True:
            try:
                id = int(input("choisissez un indice : "))
            except ValueError:
                print("vous devez entrer un entier")
            else:
                if id in id_list:
                    break
                else:
                    print("vous devez entrer un indice existant")
        return id
