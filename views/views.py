import os


class Views:
    """mother class for MenuView,PlayerView and TournamentView"""

    clean_system_command = "cls" if os.name == "nt" else "clear"

    def __init__(self, view_name):
        self.view_name = view_name

    def clear_console(self, tournament_name=""):
        os.system(self.clean_system_command)
        print("############ CHESS PROGRAM ############")
        print()
        if tournament_name:
            print("Tournoi sélectionné :", tournament_name)
            print()

    def message(self, message):
        print(message)

    def display_line(self, line, display_name):
        form = self.format_line_display[display_name]
        print(form.format(*[str(arg) for arg in line]))

    def display_list(self, list_to_display, id=False, order="", title="", display_name=""):
        if not title:
            print(self.title_display[display_name], order)
        else:
            print(title)

        id_name = ""
        if id:
            id_name = "ID"

        print()
        self.display_line(
            [id_name] + list(self.columns_name_dict[display_name].values()),
            display_name,
        )
        if id_name:
            for record in list_to_display:
                self.display_line([record.doc_id] + [value for value in record.values()], display_name)

        else:
            for record in list_to_display:
                self.display_line([""] + [value for value in record.values()], display_name)
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
