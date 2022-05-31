class Matches:
    def __init__(
        self, first_player, second_player, result_first_player, result_second_player
    ):
        self.match = (
            [first_player, result_first_player],
            [second_player, result_second_player],
        )
        print(
            f"résultat du match {first_player.last_name} , {second_player.last_name} = {result_first_player} , {result_second_player}"
        )
