class Players:
    """description of the player entity"""

    def __init__(self, last_name, first_name, birth_date, gender, ranking, id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.id = id

    def serialized_player(self):
        return dict(self.__dict__)
