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
            "first_player": "Nom Prénom",
            "result_first_player": "Score",
            "second_player": "Nom Prénom",
            "result_second_player": "Score",
        },
        "matches_to_play_display": {
            "round_name": "Nom de la ronde",
            "match": "Matchs à jouer",
        },
        "tournament_ranking_display": {
            "score": "Score",
            "name": "Nom Prénom",
            "ranking": "Classement",
        },
    }

    format_line_display = {
        "tournaments_display": "{0:^8}{1:17}{2:17}{3:17}{4:^8}{6:15}{8:30}",
        "rounds_display": "{0:^8}{1:17}{2:25}{3:25}",
        "matches_display": "{0:^8}{1:^20}{3:^7}{2:25}{5:^7}{4:25}",
        "matches_to_play_display": "{0:^8}{1:20}{2:30}",
        "tournament_ranking_display": "{0:^8}{1:^7}{2:25}{3:^10}",
    }
    title_display = {
        "tournaments_display": "Liste des tournois",
        "rounds_display": "Liste des rondes du tournoi",
        "matches_display": "Liste des matchs du tournoi",
        "matches_to_play_display": "Liste des matchs à jouer",
        "tournament_ranking_display": "Classement des joueurs dans le tournoi",
    }

    def __init__(self):
        super().__init__("tournaments")

    def message(self, message):
        print(message)

    def input_tournament(self):
        data = {}
        data["name"] = input("Nom du tournoi : ")
        data["location"] = input("Lieu du tournoi : ")
        while True:
            entry = input("Date du tournoi (JJ/MM/AAAA) : ")
            if (
                re.match(
                    r"(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1\d|0[1-9]|1[012])\/(19|20)\d\d",
                    entry,
                )
                is not None
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

    def input_result(self, first_player, match):

        while True:
            entry = input(
                f"Dans le match {match}, merci de saisir le résultat de {first_player} : "
            )
            if entry in ["V", "E", "P"]:
                return entry
