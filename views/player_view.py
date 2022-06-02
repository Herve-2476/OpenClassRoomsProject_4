import re


class PlayerView:
    correspondence_db_display_dict = {
        "last_name": "Nom",
        "first_name": "Prénom",
        "birth_date": "Date de naissance",
        "gender": "Sexe",
        "ranking": "Classement",
    }

    def display_line(self, line):
        form = "{0:^8}{1:15}{2:15}{3:20}{4:8}{5:^12}"
        print(form.format(*line))

    def display_players_list(self, players_list, correspondence_players_dict=[]):

        id_name = ""
        if correspondence_players_dict:
            id_name = "ID"

        if players_list:
            print()
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

    def input_player(self):
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
        id = int(input("Entrez l'ID du jouer/joueuse à modifier : "))
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
