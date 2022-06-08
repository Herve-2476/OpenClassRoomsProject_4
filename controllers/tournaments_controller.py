from views.tournament_view import TournamentView


class TournamentsController:
    def __init__(self, db, players_controller):
        self.tournament_view = TournamentView()
        self.db = db
        self.table = db.table("tournaments")
        self.players_number = 8
        self.id_selected_tournament = 0
        self.name_selected_tournament = ""
        self.players_controller = players_controller
        # table.truncate()
        # table.remove(doc_ids=[11])

    def display_tournaments_list(self):
        table = self.db.load_all(self.table)
        self.tournament_view.display_db_list(table)
        return [record.doc_id for record in table]

    def load_tournament(self):
        self.tournament_view.clear_console(self.name_selected_tournament)
        id_tournaments_list = self.display_tournaments_list()
        while True:
            id_choice = self.tournament_view.id_choice(id_tournaments_list)
            if id_choice in id_tournaments_list:
                break

        self.id_selected_tournament = id_choice
        self.name_selected_tournament = (
            self.db.get_id(self.table, id_choice)["name"]
            + " à "
            + self.db.get_id(self.table, id_choice)["location"]
            + " le "
            + self.db.get_id(self.table, id_choice)["date"]
        )
        self.tournament_view.clear_console(self.name_selected_tournament)

    def add_tournament(self):
        tournament = self.tournament_view.input_tournament()
        id_players_list = self.players_controller.display_players_list()
        tournament["players_list"] = self.tournament_view.input_tournament_players_list(
            id_players_list, self.players_number
        )
        self.db.insert(self.table, tournament)
        self.tournament_view.clear_console()
