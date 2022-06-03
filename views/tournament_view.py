import re


class TournamentView:
    correspondence_db_display_dict = {
        "name": "Nom du tournoi",
        "location": "Lieu du tournoi",
        "date": "Date du tournoi",
        "rounds_number": "Nombre de tours",
        "rounds": "Tournées",
        "players_list": "Liste des joueurs",
        "time_control": "Contrôle du temps",
        "description": "Remarques du Directeur",
    }

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

        return data
