from models.players_table import PlayersTable
from models.players import Players
from views.player_view_old import PlayerView


# import tests.functions


# tests.functions.data_players_creation(PlayersTable())


class PlayersManagerNew:
    def __init__(self, table):
        self.player_view = PlayerView()
        self.table = table

    def display_players_list(self, ordre="Alphabétique"):
        table = self.table.all()
        table.sort(key=lambda x: x["ranking"])
        if ordre == "Alphabétique":
            table.sort(key=lambda x: x["first_name"])
            table.sort(key=lambda x: x["last_name"])

        self.player_view.display_db_list(table, ordre=ordre)
        return [record.doc_id for record in table]


class PlayersManager:
    def __init__(self):
        pass

    def load_players_list(self, players_table):
        players_list_serialized = players_table.all()
        correspondence_players_dict = {}
        players_list = []
        for player in players_list_serialized:
            deserialized_player = self.deserialized_player(player)
            players_list.append(deserialized_player)
            correspondence_players_dict[deserialized_player] = player.doc_id

        return players_list, correspondence_players_dict

    def save_players(self, players_list):
        PlayersTable().save(players_list)

    def deserialized_player(self, player):
        last_name = player["last_name"]
        first_name = player["first_name"]
        birth_date = player["birth_date"]
        gender = player["gender"]
        ranking = player["ranking"]

        return Players(
            last_name=last_name,
            first_name=first_name,
            birth_date=birth_date,
            gender=gender,
            ranking=ranking,
        )

    def sort_in_alphabetical_order(self, players_list):
        """sort in alphabetical order"""
        players_list = [
            (player.last_name, player.first_name, player.ranking, player)
            for player in players_list
        ]
        players_list.sort(key=lambda x: x[2])
        players_list.sort(key=lambda x: x[1])
        players_list.sort(key=lambda x: x[0])
        return [player[3] for player in players_list], "ORDRE ALPHABETIQUE"

    def sort_in_ranking_order(self, players_list):
        """sort in ranking order"""
        players_list = [(player.ranking, player) for player in players_list]
        players_list.sort(key=lambda x: x[0])
        return [player[1] for player in players_list], "CLASSEMENT"

    def add_player(self, players_table):
        player = PlayerView().input_player()
        players_table.insert(player)

    def modify_data_player(self, players_table, correspondence_players_list):
        serialized_player, id_player = PlayerView().modify_data_player(
            correspondence_players_list
        )
        players_table.update(serialized_player, doc_ids=[id_player])