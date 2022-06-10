import re
from views.views import Views


class TournamentView(Views):
    columns_name_dict = {
        "tournaments_display": {
            "name": "Nom du tournoi",
            "location": "Lieu du tournoi",
            "date": "Date du tournoi",
            "rounds_number": "Tours",
            "rounds_list": "Tournées",
            "time_control": "Ctrl Temps",
            "players_list": "Liste des joueurs",
            "description": "Description",
        },
        "rounds_display": {
            "name": "Nom de la ronde",
            "start_time_round": "Début de la ronde",
            "end_time_round": "Fin de la ronde",
        },
        "matches_display": {
            "round_name": "Nom de la ronde",
            "first_player": "Nom Prénom, Score",
            "second_player": "Nom Prénom, Score",
            "match": "('Nom Prénom, Score','Nom Prénom, Score')",
        },
    }

    format_line_display = {
        "tournaments_display": "{0:^8}{1:17}{2:17}{3:17}{4:^8}{6:15}{8:30}",
        "rounds_display": "{0:^8}{1:17}{2:20}{3:20}",
        "matches_display": "{0:^8}{1:20}{2:30}{3:30}",
    }
    title_display = {
        "tournaments_display": "Liste des tournois",
        "rounds_display": "Liste des rondes du tournoi",
        "matches_display": "Liste des matchs du tournoi",
    }

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
