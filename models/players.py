class Players:
    """to create a player instance"""

    def __init__(self, last_name, first_name, birth_date, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

    def serialized_player(self):
        return self.__dict__
