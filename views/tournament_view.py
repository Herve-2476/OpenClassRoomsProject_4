class TournamentView:
    def input_tournament(self):
        data = {}
        data["name"] = input("Nom du tournoi : ")
        data["location"] = input("Lieu : ")
        data["tournament_date"] = input("Date du tournoi (JJ/MM/AAAA) : ")
        return data
