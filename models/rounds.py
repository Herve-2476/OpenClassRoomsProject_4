import datetime

from .matches import Matches


class Rounds:
    """description of a round"""

    def __init__(
        self, name="", start_time_round=None, end_time_round=None, matches_list=[]
    ):

        self.matches_list = self.matches_instantiation(matches_list)
        self.name = name
        self.start_time_round = start_time_round
        self.end_time_round = end_time_round

    def matches_instantiation(self, matches_list):

        return [
            Matches(first_player, second_player)
            for first_player, second_player in matches_list
        ]

    def start_round(self):
        self.start_time_round = datetime.datetime.today()
        print("start at", self.end_time_round.strftime("%Y-%m-%d %H:%M:%S"))

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

    def display(self):
        for match in self.matches_list:
            print(match.display())

    @property
    def round_started(self):
        if hasattr(self, "start_time_round"):
            return True
        else:
            return False

    @property
    def round_finished(self):
        if hasattr(self, "start_end_round"):
            return True
        else:
            return False
