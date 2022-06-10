import re
from views.player_view import PlayerView


class PlayersController:
    def __init__(self, db):
        self.player_view = PlayerView()
        self.db = db
        self.table = db.table("players")
        self.date_regex = (
            "(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1\d|0[1-9]|1[012])\/(19|20)\d\d"
        )

    def display_players_list(self, order="", **args):
        self.player_view.clear_console()
        table = self.db.load_all(self.table)
        table.sort(key=lambda x: x["ranking"])
        if order == "ordre Alphabétique":
            table.sort(key=lambda x: x["first_name"])
            table.sort(key=lambda x: x["last_name"])

        self.player_view.display_db_list(table, order=order, **args)
        return [record.doc_id for record in table]

    def add_player(self):
        self.player_view.clear_console()
        while True:
            player = self.player_view.input_player()
            if self.control_data_player(player):
                break

        self.db.insert(self.table, player)
        self.player_view.clear_console()

    def modify_player(self):
        self.player_view.clear_console()
        id_list = self.display_players_list(
            order="ordre Alphabétique", display_name="players_display"
        )
        while True:
            id_choice = self.player_view.id_choice(id_list)
            if id_choice in id_list:
                break
        player = self.db.get_id(self.table, id_choice)

        while True:
            player = self.player_view.modify_player(player)
            if self.control_data_player(player):
                break
        self.db.update_id(self.table, id_choice, player)
        self.player_view.clear_console()

    def control_data_player(self, player):
        control = [
            isinstance(player["last_name"], str),
            isinstance(player["first_name"], str),
            re.match(self.date_regex, player["birth_date"]),
            player["gender"] in ["M", "F"],
            isinstance(player["ranking"], int),
        ]

        return all(control)

    def matches_to_play_list(self):
        if self.tournament.rounds_list:
            pass
        else:
            self.tournament.first_round_generation()
