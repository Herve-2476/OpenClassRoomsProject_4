import re
from views.views import Views


class PlayerView(Views):

    columns_name_dict = {
        "players_display": {
            "last_name": "Nom",
            "first_name": "Prénom",
            "birth_date": "Date de naissance",
            "gender": "Sexe",
            "ranking": "Classement",
        }
    }
    format_line_display = {"players_display": "{0:^8}{1:15}{2:15}{3:20}{4:8}{5:^12}"}
    title_display = {"players_display": "Liste des joueurs par"}

    def __init__(self):
        super().__init__("players")

    def input_player(self):
        print("Saisie d'un nouveau joueur")
        print()
        player = {}
        player["last_name"] = input("Nom : ")
        player["first_name"] = input("Prénom : ")

        while True:
            entry = input("Date de naissance (JJ/MM/AAAA) : ")

            if (
                re.match(
                    r"(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1\d|0[1-9]|1[012])\/(19|20)\d\d",
                    entry,
                )
                is not None
            ):
                player["birth_date"] = entry
                break

        while True:
            entry = input("Sexe : ")
            if entry in ["M", "F"]:
                player["gender"] = entry
                break

        while True:
            entry = input("Classement : ")
            if (
                re.match(
                    r"\d+",
                    entry,
                )
                is not None
            ):
                player["ranking"] = int(entry)
                break

        return player

    def modify_player(self, player):
        """modify a player in dict format"""

        entry = input("Nom : " + player["last_name"] + " ")
        if entry != "":
            player["last_name"] = entry
        entry = input("Prénom : " + player["first_name"] + " ")
        if entry != "":
            player["first_name"] = entry

        while True:
            entry = input(
                "Date de naissance (JJ/MM/AAAA) : " + player["birth_date"] + " "
            )
            if entry == "":
                break
            elif (
                re.match(
                    r"(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1\d|0[1-9]|1[012])\/(19|20)\d\d",
                    entry,
                )
                is not None
            ):
                player["birth_date"] = entry
                break

        while True:
            entry = input("Sexe : " + player["gender"] + " ")
            if entry == "":
                break

            elif entry in ["M", "F"]:
                player["gender"] = entry
                break
        while True:
            entry = input("Classement : " + str(player["ranking"]) + " ")
            if entry == "":
                break
            elif (
                re.match(
                    r"\d+",
                    entry,
                )
                is not None
            ):
                player["ranking"] = int(entry)
                break

        return player
