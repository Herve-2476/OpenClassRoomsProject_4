from .players import Players
from .models import Models


class Matches:
    def __init__(
        self,
        first_player,
        second_player,
        result_first_player=None,
        result_second_player=None,
    ):

        self.match = [
            [
                first_player,
                result_first_player,
            ],
            [
                second_player,
                result_second_player,
            ],
        ]

    @property
    def serialized(self):
        return (
            [self.match[0][0].id, self.match[0][1]],
            [self.match[1][0].id, self.match[1][1]],
        )

    def add_score(self, result_first_player, result_second_player):
        self.match[0][1] = result_first_player
        self.match[1][1] = result_second_player
