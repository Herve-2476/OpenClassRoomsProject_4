import re
from views.views_old import Views


class PlayerView(Views):
    correspondence_db_display_dict = {
        "last_name": "Nom",
        "first_name": "Prénom",
        "birth_date": "Date de naissance",
        "gender": "Sexe",
        "ranking": "Classement",
    }
    columns_name_dict = {
        "last_name": "Nom",
        "first_name": "Prénom",
        "birth_date": "Date de naissance",
        "gender": "Sexe",
        "ranking": "Classement",
    }
    format_line_display = "{0:^8}{1:15}{2:15}{3:20}{4:8}{5:^12}"
    title_display = "Liste des joueurs par"

    def __init__(self):
        super().__init__("players")

    def input_player(self):
        print("Saisie d'un nouveau joueur")
        print()
        data = {}
        data["last_name"] = input("Nom : ")
        data["first_name"] = input("Prénom : ")

        while True:
            entry = input("Date de naissance (JJ/MM/AAAA) : ")
            if (
                re.match(
                    "(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1\d|0[1-9]|1[012])\/(19|20)\d\d",
                    entry,
                )
                != None
            ):
                data["birth_date"] = entry
                break

        while True:
            entry = input("Sexe : ")
            if entry in ["M", "F"]:
                data["gender"] = entry
                break

        while True:
            entry = input("Classement : ")
            if (
                re.match(
                    "\d+",
                    entry,
                )
                != None
            ):
                data["ranking"] = int(entry)
                break

        return data

    def modify_data_player(self, correspondence_players_dict):
        print("Modification d'un joueur/joueuse")
        print()
        while True:
            try:
                id = int(input("choisissez un indice : "))
            except ValueError:
                print("vous devez entrer un entier")
            else:
                if id in correspondence_players_dict.values():
                    break
                else:
                    print("vous devez entrer un indice existant")
        index = list(correspondence_players_dict.values()).index(id)
        player = list(correspondence_players_dict.keys())[index]
        data = {}

        entry = input("Nom : " + player.last_name + " ")
        data["last_name"] = player.last_name if entry == "" else entry
        entry = input("Prénom : " + player.first_name + " ")
        data["first_name"] = player.first_name if entry == "" else entry

        while True:
            entry = input("Date de naissance (JJ/MM/AAAA) : " + player.birth_date + " ")
            if entry == "":
                data["birth_date"] = player.birth_date
                break
            elif (
                re.match(
                    "(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1\d|0[1-9]|1[012])\/(19|20)\d\d",
                    entry,
                )
                != None
            ):
                data["birth_date"] = entry
                break

        while True:
            entry = input("Sexe : " + player.gender + " ")
            if entry == "":
                data["gender"] = player.gender
                break

            elif entry in ["M", "F"]:
                data["gender"] = entry
                break
        while True:
            entry = input("Classement : " + str(player.ranking) + " ")
            if entry == "":
                data["ranking"] = player.ranking
                break
            elif (
                re.match(
                    "\d+",
                    entry,
                )
                != None
            ):
                data["ranking"] = int(entry)
                break

        return data, id
