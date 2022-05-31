import datetime
import time
import random

from matches import Matches


class Rounds:
    """description of a round"""

    def __init__(self, players_pair_list, round_counter):
        self.players_pair_list = players_pair_list
        self.matches_list = []
        self.name = f"Round {round_counter}"
        print(self.name)
        self.start_time_round = datetime.datetime.today()
        print(self.start_time_round.strftime("%Y-%m-%d %H:%M:%S"))
        self.input_results()
        # time.sleep(1)
        self.end_time_round = datetime.datetime.today()
        print(self.end_time_round.strftime("%Y-%m-%d %H:%M:%S"))

    def input_results(self):
        result_list = round_result(len(self.players_pair_list))

        for (player_one, player_two), (result_one, result_two) in zip(
            self.players_pair_list, result_list
        ):

            self.matches_list.append(
                Matches(player_one, player_two, result_one, result_two)
            )


def round_result(n):
    result_list = []
    for i in range(n):
        result = random.randint(0, 2)
        if result == 0:
            result_list.append((1, 0))
        elif result == 1:
            result_list.append((0.5, 0.5))
        else:
            result_list.append((0, 1))
    return result_list
