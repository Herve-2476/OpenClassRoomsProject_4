from tinydb import TinyDB

# from tournaments import Tournaments
# from players import Players
# from players_table import PlayersTable
# import data
# import random

# import pickle


class Models(TinyDB):
    def __init__(self):
        super().__init__("db.json")

    def load_all(self, table):
        return table.all()

    def save(self):
        pass


if __name__ == "__main__":

    tournament = Tournaments(
        "tournament_1",
        "Bordeaux",
        "30/05/2022",
        "Nice day to play",
        "bullet",
    )

    index_list_players = random.sample(range(len(data.players)), 8)
    index_list_players = range(len(data.players))
    rank_players_list = []
    for index_player in index_list_players:
        ranking = data.players[index_player]["ranking"]
        rank_players_list.append(
            (
                ranking,
                Players(
                    last_name=data.players[index_player]["last_name"],
                    first_name=data.players[index_player]["first_name"],
                    birthday_date=data.players[index_player]["birthday_date"],
                    gender=data.players[index_player]["gender"],
                    ranking=data.players[index_player]["ranking"],
                ),
            )
        )

    players_list = []
    for _, player in sorted(rank_players_list):
        players_list.append(player)
