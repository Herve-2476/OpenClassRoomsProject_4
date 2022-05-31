import datetime
import time
import random

from .matches import Matches


class Rounds:
    """description of a round"""

    def __init__(self, players_pair_list, round_counter):
        self.players_pair_list = players_pair_list
        self.matches_list = []
        self.name = f"Round {round_counter}"
        print(self.name)
        self.start_time_round = datetime.datetime.today()
        print("start at", self.start_time_round.strftime("%Y-%m-%d %H:%M:%S"))

        # self.input_results()
        # time.sleep(1)

    def end_round(self):
        self.end_time_round = datetime.datetime.today()
        print("end at", self.end_time_round.strftime("%Y-%m-%d %H:%M:%S"))

    def input_results(self, result_list):

        for (player_one, player_two), (result_one, result_two) in zip(
            self.players_pair_list, result_list
        ):

            self.matches_list.append(
                Matches(player_one, player_two, result_one, result_two)
            )
