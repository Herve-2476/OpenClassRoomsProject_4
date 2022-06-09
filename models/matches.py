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
        args_first_player = db.get_id(db.table("players"), first_player)
        args_first_player["id"] = first_player
        args_second_player = db.get_id(db.table("players"), second_player)
        args_second_player["id"] = second_player

        self.match = [
            [
                Players(**args_first_player),
                result_first_player,
            ],
            [
                Players(**args_second_player),
                result_second_player,
            ],
        ]

    @property
    def serialized(self):
        return (
            [self.match[0][0].id, self.match[0][1]],
            [self.match[1][0].id, self.match[1][1]],
        )
