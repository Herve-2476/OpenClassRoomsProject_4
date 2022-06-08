import os


class Views:
    clean_system_command = "cls" if os.name in ("nt", "dos") else "clear"
    view_dict = {
        "players": {
            "form": "{0:^8}{1:15}{2:15}{3:20}{4:8}{5:^12}",
            "title": "Liste des joueurs par",
        },
        "tournaments": {
            "form": "{0:^8}{1:20}{2:20}{3:20}{4:8}{5:^12}",
            "title": "Liste des tournois",
        },
    }

    def __init__(self, view_name):
        self.view_name = view_name

    def clear_console(self, tournament_name=""):
        os.system(self.clean_system_command)
        print("############ CHESS PROGRAM ############")
        print()
        if tournament_name:
            print("Tournoi en cours :", tournament_name)
            print()

    def display_line(self, line):

        form = self.view_dict[self.view_name]["form"]
        print(form.format(*line))

    def display_line_1(self, line):
        form = self.format_line_display
        print(form.format(*[str(e) for e in line]))

    def display_players_list(self, players_list_title, correspondence_players_dict=[]):
        players_list, title = players_list_title
        print(self.view_dict[self.view_name]["title"], title)
        print()

        id_name = ""
        if correspondence_players_dict:
            id_name = "ID"

        if players_list:

            self.display_line(
                [id_name] + list(self.correspondence_db_display_dict.values())
            )
            print()
            if correspondence_players_dict:
                for player in players_list:
                    self.display_line(
                        [correspondence_players_dict[player]]
                        + [
                            player.__dict__[key]
                            for key in self.correspondence_db_display_dict.keys()
                        ]
                    )
            else:

                for player in players_list:
                    self.display_line(
                        [""]
                        + [
                            player.__dict__[key]
                            for key in self.correspondence_db_display_dict.keys()
                        ]
                    )
            print()

    def display_db_list(self, db_table_list, id=True, ordre=""):
        self.clear_console()
        print(self.title_display, ordre)
        print()
        id_name = ""
        if id:
            id_name = "ID"

        if db_table_list:

            self.display_line_1([id_name] + list(self.columns_name_dict.values()))
            print()
            if id_name:
                for record in db_table_list:
                    self.display_line_1(
                        [record.doc_id] + [value for value in record.values()]
                    )
            else:

                for record in db_table_list:
                    self.display_line_1([""] + [value for value in record.values()])
            print()

    def id_input(self, id_list):
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