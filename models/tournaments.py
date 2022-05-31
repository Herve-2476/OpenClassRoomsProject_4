from .rounds import Rounds


class Tournaments:
    """to create an tournament instance"""

    def __init__(
        self,
        name,
        location,
        date,
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
        self.players_list = []
        self.description = description
        self.matches_list = []
        self.players_dict = {}

    def add_player(self, player):
        self.players_list.append(player)

    def score_display(self, ranked_players_point_list):
        for e in ranked_players_point_list:
            print(
                f"{e[2].last_name} a {e[0]} points dans le tournoi et est classé {e[1]}"
            )

    def first_round_generation(self):
        players_pair_list = []
        half_players_number = int(len(self.players_list) / 2)

        for i in range(half_players_number):
            players_pair_list.append(
                (self.players_list[i], self.players_list[i + half_players_number])
            )

        self.rounds_list.append(Rounds(players_pair_list, len(self.rounds_list) + 1))

    def ranking_players_after_round(self):

        for match in self.rounds_list[-1].matches_list:
            player_one = match.match[0][0]
            player_two = match.match[1][0]
            result_one = match.match[0][1]
            result_two = match.match[1][1]
            self.matches_list.append((player_one, player_two))
            self.players_dict[player_one] = (
                self.players_dict.get(player_one, 0) + result_one
            )
            self.players_dict[player_two] = (
                self.players_dict.get(player_two, 0) + result_two
            )
        ranked_players_list = []
        for key, value in self.players_dict.items():
            ranked_players_list.append((value, key.ranking, key))
        ranked_players_list.sort(key=lambda x: x[1])
        ranked_players_list.sort(key=lambda x: x[0], reverse=True)
        ranked_players_point_list = list(ranked_players_list)
        ranked_players_list = [player[2] for player in ranked_players_list]

        return ranked_players_list, self.matches_list, ranked_players_point_list

    def following_round_generation(self, ranked_players_list, matches_list):

        players_pair_list = []
        while ranked_players_list:
            j = 1
            # print("j = ", j, ranked_players_list)
            while (ranked_players_list[0], ranked_players_list[j]) in matches_list or (
                ranked_players_list[j],
                ranked_players_list[0],
            ) in matches_list:
                # print("égalité trouvée")
                if j == len(ranked_players_list) - 1:
                    # print("on est allé jusqu'au bout")
                    break
                j += 1
            players_pair_list.append((ranked_players_list[0], ranked_players_list[j]))
            ranked_players_list.remove(ranked_players_list[j])
            ranked_players_list.remove(ranked_players_list[0])

        # for e in players_pair_list:
        # print(e)

        self.rounds_list.append(Rounds(players_pair_list, len(self.rounds_list) + 1))
