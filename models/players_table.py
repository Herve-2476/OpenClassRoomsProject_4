import pickle
import os


class PlayersTable:
    players_table_file_name = "models/tables/players_table.dat"

    def __init__(self):
        print(os.getcwd())
        if os.path.exists(self.players_table_file_name):
            self.load()

    def save(self, players_table_list):
        with open(self.players_table_file_name, "wb") as f:
            pickle.dump(players_table_list, f)

    def load(self):
        with open(self.players_table_file_name, "rb") as f:
            return pickle.load(f)
