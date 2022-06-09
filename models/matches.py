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
        db = Models()

        self.match = (
            [
                Players(**db.get_id(db.table("players"), first_player)),
                result_first_player,
            ],
            [
                Players(**db.get_id(db.table("players"), second_player)),
                result_second_player,
            ],
        )

    def display(self):
        return (
            self.match[0][0].serialized_player(),
            self.match[1][0].serialized_player(),
        )
