import datetime

from .matches import Matches


class Rounds:
    """description of a round"""

    def __init__(
        self, name="", start_time_round=None, end_time_round=None, matches_list=[]
    ):

        if isinstance(matches_list[0][0], list):  # score exist
            self.matches_list = []
            for match in matches_list:
                first_player = match[0][0]
                second_player = match[1][0]
                result_first_player = match[0][1]
                result_second_player = match[1][1]
                self.matches_list.append(
                    Matches(
                        first_player,
                        second_player,
                        result_first_player,
                        result_second_player,
                    )
                )

        else:
            self.matches_list = [
                Matches(first_player, second_player)
                for first_player, second_player in matches_list
            ]

        self.name = name
        self.start_time_round = start_time_round
        self.end_time_round = end_time_round

    def matches_instantiation(self, matches_list):

        if isinstance(matches_list[0][0], int):  # player_id
            return [
                Matches(first_player, second_player)
                for first_player, second_player in matches_list
            ]

        else:  # player_object
            # add score
            return_list = []
            for match in matches_list:
                first_player = match[0][0]
                second_player = match[1][0]
                result_first_player = match[0][1]
                result_second_player = match[1][1]
                return_list.append(
                    Matches(
                        first_player,
                        second_player,
                        result_first_player,
                        result_second_player,
                    )
                )

            return return_list

    def start_round(self):
        self.start_time_round = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
        return f"Ronde {self.name} commencée le {self.start_time_round}"

    def end_round(self):
        self.end_time_round = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")

    def input_results(self, result_list):

        for (player_one, player_two), (result_one, result_two) in zip(
            self.players_pair_list, result_list
        ):

            self.matches_list.append(
                Matches(player_one, player_two, result_one, result_two)
            )

    @property
    def serialized(self):
        serialized_dict = {
            "name": self.name,
            "start_time_round": self.start_time_round,
            "end_time_round": self.end_time_round,
            "matches_list": [match.serialized for match in self.matches_list],
        }
        return serialized_dict

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
