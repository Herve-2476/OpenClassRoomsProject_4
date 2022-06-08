import re
from views.views import Views


class TournamentView(Views):
    columns_name_dict = {
        "name": "Nom du tournoi",
        "location": "Lieu du tournoi",
        "date": "Date du tournoi",
        "time_control": "Ctrl Temps",
        "description": "Description",
        "rounds_number": "Tours",
        "rounds": "Tournées",
        "players_list": "Liste des joueurs",
    }

    format_line_display = "{0:^8}{1:17}{2:17}{3:17}{6:^8}{4:15}{5:30}"
    title_display = "Liste des tournois"

    def __init__(self):
        super().__init__("tournaments")

    def input_tournament(self):
        data = {}
        data["name"] = input("Nom du tournoi : ")
        data["location"] = input("Lieu du tournoi : ")
        while True:
            entry = input("Date du tournoi (JJ/MM/AAAA) : ")
            if (
                re.match(
                    "(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1\d|0[1-9]|1[012])\/(19|20)\d\d",
                    entry,
                )
                != None
            ):
                data["date"] = entry
                break
        while True:
            entry = input("Contrôle du temps (bullet,blitz ou coup rapide) : ")
            if entry in ["bullet", "blitz", "coup rapide"]:
                data["time_control"] = entry
                break
        data["description"] = input("Description : ")

        return data

    def input_tournament_players_list(self, id_players_list, players_number):
        print(f"Vous devez entrer les IDs de {players_number} joueurs")
        tournament_players_set = set()
        while len(tournament_players_set) < players_number:
            tournament_players_set.add(self.id_choice(id_players_list, title=""))

        return list(tournament_players_set)
