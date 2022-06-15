import datetime

from .matches import Matches


class Rounds:
    """
    description of the round entity which is
    itself composed of match entities
    """

    def __init__(self, name="", start_time_round=None, end_time_round=None, matches_list=[]):

        if isinstance(matches_list[0][0], list):  # score exists
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
            self.matches_list = [Matches(first_player, second_player) for first_player, second_player in matches_list]

        self.name = name
        self.start_time_round = start_time_round
        self.end_time_round = end_time_round

    def start_round(self):
        self.start_time_round = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
        return f"Ronde {self.name} commencée le {self.start_time_round}"

    def end_round(self):
        self.end_time_round = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")

    @property
    def serialized(self):
        serialized_dict = {
            "name": self.name,
            "start_time_round": self.start_time_round,
            "end_time_round": self.end_time_round,
            "matches_list": [match.serialized for match in self.matches_list],
        }
        return serialized_dict
