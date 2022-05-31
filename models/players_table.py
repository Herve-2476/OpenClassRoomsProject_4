from copyreg import pickle
import os


class PlayersTable:
    players_table_file_name = "players_table.dat"
    players_table_list = []

    def __init__(self):
        if os.path.exits(self.players_table_file_name):
            self.load(self.players_table_file_name)

    def save(self):
        with open(self.players_table_file_name, "wb") as f:
            pickle.dump(self.players_table_list)

    def load(self):
        with open(self.players_table_file_name, "rb") as f:
            self.players_table_list = pickle.load(f)
