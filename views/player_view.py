class PlayerView:
    correspondence_column_title_dict = {
        "last_name": "Nom",
        "first_name": "Prénom",
        "birthday_date": "Date de naissance",
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
                [id_name] + list(self.correspondence_column_title_dict.values())
            )
            print()
            if correspondence_players_dict:
                for player in players_list:
                    self.display_line(
                        [correspondence_players_dict[player]]
                        + [
                            player.__dict__[key]
                            for key in self.correspondence_column_title_dict.keys()
                        ]
                    )
            else:
                for player in players_list:
                    self.display_line(
                        [""]
                        + [
                            player.__dict__[key]
                            for key in self.correspondence_column_title_dict.keys()
                        ]
                    )

    def input_player(self):
        data = {}
        data["last_name"] = input("Nom : ")
        data["first_name"] = input("Prénom : ")
        data["birthday_date"] = input("Date de naissance (JJ/MM/AAAA) : ")
        data["gender"] = input("Sexe : ")
        data["ranking"] = int(input("Classement : "))
        return data

    def modify_data_player(self, correspondence_players_dict):
        id = int(input("Entrez l'ID du jouer/joueuse à modifier : "))
        index = list(correspondence_players_dict.values()).index(id)
        player = list(correspondence_players_dict.keys())[index]
        data = {}

        var = input("Nom : " + player.last_name + " ")
        data["last_name"] = player.last_name if var == "" else var
        var = input("Prénom : " + player.first_name)
        data["first_name"] = player.first_name if var == "" else var
        var = input("Date de naissance (JJ/MM/AAAA) : " + player.birthday_date)
        data["birthday_date"] = player.birthday_date if var == "" else var
        var = input("Sexe : " + player.gender)
        data["gender"] = player.gender if var == "" else var
        var = input("Classement : " + str(player.ranking))
        data["ranking"] = player.ranking if var == "" else int(var)
        return data, id
