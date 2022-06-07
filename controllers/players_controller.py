from views.player_view import PlayerView


class PlayersController:
    def __init__(self, db):
        self.player_view = PlayerView()
        self.db = db
        self.table = db.table("players")

    def display_players_list(self, order=""):
        self.player_view.clear_console()
        table = self.db.load_all(self.table)
        table.sort(key=lambda x: x["ranking"])
        if order == "ordre Alphabétique":
            table.sort(key=lambda x: x["first_name"])
            table.sort(key=lambda x: x["last_name"])

        self.player_view.display_db_list(table, order=order)
        return [record.doc_id for record in table]
