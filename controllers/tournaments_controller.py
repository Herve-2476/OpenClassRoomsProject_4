from views.tournament_view import TournamentView


class TournamentsController:
    def __init__(self, db):
        self.tournament_view = TournamentView()
        self.db = db
        self.table = db.table("tournaments")
        self.players_number = 8
        # table.truncate()
        # table.remove(doc_ids=[11])

    def display_tournaments_list(self):
        self.tournament_view.display_db_list(self.db.load_all(self.table))
