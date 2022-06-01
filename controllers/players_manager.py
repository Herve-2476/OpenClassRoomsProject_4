from models.players_table import PlayersTable
from models.players import Players
from views.player_view import PlayerView


# import tests.functions


# tests.functions.data_players_creation(PlayersTable())


class PlayersManager:
    def __init__(self):
        pass

    def load_players_list(self):
        list_players = PlayersTable().load()
        list_players = [
            self.dico_player_to_object_player(player) for player in list_players
        ]
        return list_players

    def save_players(self, list_players):
        PlayersTable().save(list_players)

    def dico_player_to_object_player(self, player):
        last_name = player["last_name"]
        first_name = player["first_name"]
        birthday_date = player["birthday_date"]
        gender = player["gender"]
        ranking = player["ranking"]

        return Players(
            last_name=last_name,
            first_name=first_name,
            birthday_date=birthday_date,
            gender=gender,
            ranking=ranking,
        )

    def sort_in_alphabetical_order(self, list_players):
        ###sort in alphabetical order###
        list_players = [
            (player.last_name, player.first_name, player.ranking, player)
            for player in list_players
        ]
        list_players.sort(key=lambda x: x[2])
        list_players.sort(key=lambda x: x[1])
        list_players.sort(key=lambda x: x[0])
        return [player[3] for player in list_players]

    def sort_in_ranking_order(self, list_players):
        ###sort in ranking order###
        list_players = [(player.ranking, player) for player in list_players]
        list_players.sort()
        return [player[1] for player in list_players]

    def add_player(self):
        player = PlayerView().input_player()
        list_players = PlayersTable().load()
        list_players.append(player)
        PlayersTable().save(list_players)
