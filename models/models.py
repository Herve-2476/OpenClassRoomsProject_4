class Tournaments:
    """to create an tournament instance"""

    def __init__(
        self, name, location, date, players_list, description, rounds_number=4
    ):
        self.name = name
        self.location = location
        self.date = date
        self.rounds_number = rounds_number
        self.rounds_list = []
        self.time_control = time_control
        self.players_list = players_list
        self.description = description


class Players:
    """to create a player instance"""

    def __init__(self, last_name, first_name, birth_date, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
