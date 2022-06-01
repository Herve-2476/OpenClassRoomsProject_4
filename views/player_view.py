class PlayerView:
    def display_line(self, line):
        form = "{0:15}{1:15}{2:15}{3:8}{4:^12}{5:^8}"
        print(form.format(*line))

    def display_players_list(self, players_list, correspondence_players_list=[]):
        id_name = ""
        if correspondence_players_list:
            id_name = "ID"

        if players_list:
            print()
            self.display_line(list(players_list[0].__dict__.keys()) + [id_name])
            print()
            if correspondence_players_list:
                for player in players_list:
                    self.display_line(
                        list(player.__dict__.values())
                        + [correspondence_players_list[player]]
                    )
            else:
                for player in players_list:
                    self.display_line(list(player.__dict__.values()) + [""])

    def input_player(self):
        data = {}
        data["last_name"] = input("Nom : ")
        data["first_name"] = input("Prénom : ")
        data["birthday_date"] = input("Date de naissance (JJ/MM/AAAA) : ")
        data["gender"] = input("Sexe : ")
        data["ranking"] = int(input("Classement : "))
        return data

    def modify_data_player(self, correspondence_players_list):
        id = int(input("Entrez l'ID du jouer/joueuse à modifier : "))
        index = list(correspondence_players_list.values()).index(id)
        player = list(correspondence_players_list.keys())[index]
        data = {}
        data["last_name"] = input("Nom : " + player.last_name)
        data["first_name"] = input("Prénom : ")
        data["birthday_date"] = input("Date de naissance (JJ/MM/AAAA) : ")
        data["gender"] = input("Sexe : ")
        data["ranking"] = int(input("Classement : "))
        assert 1 == 2
        return data
