from operator import ge


class Tournaments:
    """to create an tournament instance"""

    def __init__(
        self,
        name,
        location,
        date,
        players_list,
        description,
        time_control,
        rounds_number=4,
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

    def __init__(self, last_name, first_name, birthday_date, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday_date = birthday_date
        self.gender = gender
        self.ranking = ranking


import datetime


class Rounds:
    """description of a round"""

    def __init__(self, matches_list, name):
        self.matches_list = matches_list
        self.name = name
        self.start_time_round = datetime.datetime()
        self.end_time_round = datetime.datetime()

    def pairs_generation(self):
        pass


class Matches:
    def __init__(
        self, first_player, second_player, result_first_player, result_second_player
    ):
        pass


import data
import random

if __name__ == "__main__":

    index_list_players = random.sample(range(len(data.players)), 8)
    players_list = []
    for index_player in index_list_players:
        players_list.append(
            Players(
                last_name=data.players[index_player]["last_name"],
                first_name=data.players[index_player]["first_name"],
                birthday_date=data.players[index_player]["birthday_date"],
                gender=data.players[index_player]["gender"],
                ranking=data.players[index_player]["ranking"],
            )
        )

    tournament = Tournaments(
        "tournament_1",
        "Bordeaux",
        "30/05/2022",
        players_list,
        "Nice day to play",
        "bullet",
    )
    for e in tournament.players_list:
        print(e.last_name)
