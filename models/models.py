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
        rounds_number=8,
    ):
        self.name = name
        self.location = location
        self.date = date
        self.rounds_number = rounds_number
        self.rounds_list = []
        self.time_control = time_control
        self.players_list = players_list
        self.description = description
        self.first_round_generation()
        while len(self.rounds_list) < self.rounds_number:
            self.following_round_generation()
            # break

    def first_round_generation(self):
        players_pair_list = []
        half_players_number = int(len(self.players_list) / 2)

        for i in range(half_players_number):
            players_pair_list.append(
                (self.players_list[i], self.players_list[i + half_players_number])
            )

        self.rounds_list.append(Rounds(players_pair_list, len(self.rounds_list) + 1))

    def following_round_generation(self):
        matches_list = []
        players_dict = {}
        for round in self.rounds_list:
            for match in round.matches_list:
                player_one = match.match[0][0]
                player_two = match.match[1][0]
                result_one = match.match[0][1]
                result_two = match.match[1][1]
                matches_list.append((player_one, player_two))
                players_dict[player_one] = players_dict.get(player_one, 0) + result_one
                players_dict[player_two] = players_dict.get(player_two, 0) + result_two
        players_list = []
        for key, value in players_dict.items():
            players_list.append((value, key.ranking, key))
        players_list.sort(key=lambda x: x[1])
        players_list.sort(key=lambda x: x[0], reverse=True)
        players_list = [player[2] for player in players_list]
        # for e in players_list:
        #   print(e[0], e[1], e[2].last_name)

        for e in matches_list:
            print(e[0].last_name, e[1].last_name, sep=";", end="  ")
        print()
        players_pair_list = []
        while players_list:
            j = 1
            while (players_list[0], players_list[j]) in matches_list or (
                players_list[j],
                players_list[0],
            ) in matches_list:
                print("égalité trouvée")
                j += 1
                if j == len(players_list) - 1:
                    print("on est allé jusqu'au bout")
                    break
            players_pair_list.append((players_list[0], players_list[j]))
            players_list.remove(players_list[j])
            players_list.remove(players_list[0])

        # for e in players_pair_list:
        # print(e)

        self.rounds_list.append(Rounds(players_pair_list, len(self.rounds_list) + 1))


class Players:
    """to create a player instance"""

    def __init__(self, last_name, first_name, birthday_date, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday_date = birthday_date
        self.gender = gender
        self.ranking = ranking


import datetime
import time


class Rounds:
    """description of a round"""

    def __init__(self, players_pair_list, round_counter):
        self.players_pair_list = players_pair_list
        self.matches_list = []
        self.name = f"Round {round_counter}"
        print(self.name)
        self.start_time_round = datetime.datetime.today()
        print(self.start_time_round.strftime("%Y-%m-%d %H:%M:%S"))
        self.input_results()
        # time.sleep(1)
        self.end_time_round = datetime.datetime.today()
        print(self.end_time_round.strftime("%Y-%m-%d %H:%M:%S"))

    def input_results(self):
        result_list = round_result()

        for (player_one, player_two), (result_one, result_two) in zip(
            self.players_pair_list, result_list
        ):

            self.matches_list.append(
                Matches(player_one, player_two, result_one, result_two)
            )


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


import data
import random

result_list = []


def round_result():
    for i in range(4):
        result = random.randint(0, 2)
        if result == 0:
            result_list.append((1, 0))
        elif result == 1:
            result_list.append((0.5, 0.5))
        else:
            result_list.append((0, 1))
    return result_list


if __name__ == "__main__":

    index_list_players = random.sample(range(len(data.players)), 8)
    rank_players_list = []
    for index_player in index_list_players:
        ranking = data.players[index_player]["ranking"]
        rank_players_list.append(
            (
                ranking,
                Players(
                    last_name=data.players[index_player]["last_name"],
                    first_name=data.players[index_player]["first_name"],
                    birthday_date=data.players[index_player]["birthday_date"],
                    gender=data.players[index_player]["gender"],
                    ranking=data.players[index_player]["ranking"],
                ),
            )
        )
    players_list = []
    for _, player in sorted(rank_players_list):
        players_list.append(player)

    tournament = Tournaments(
        "tournament_1",
        "Bordeaux",
        "30/05/2022",
        players_list,
        "Nice day to play",
        "bullet",
    )
