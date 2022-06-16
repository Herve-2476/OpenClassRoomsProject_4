from .rounds import Rounds


class Tournaments:
    """
    manages the tournament entity including the Swiss system
    for the definition of matches in a round
    """

    def __init__(
        self,
        name,
        location,
        date,
        players_list,
        description,
        time_control,
        rounds_number,
        rounds_list,
    ):
        self.name = name
        self.location = location
        self.date = date
        self.rounds_number = rounds_number
        self.rounds_list = rounds_list
        self.time_control = time_control
        self.players_list = players_list
        self.description = description
        self.rounds_list = [Rounds(**round) for round in self.rounds_list]

        self.state = None
        self.matches_already_played_list = []

    def record_match(self, match, score):
        if score == "V":
            match.add_score(1, 0)
            # add_score
        elif score == "E":
            match.add_score(0.5, 0.5)
        else:
            match.add_score(0, 1)

    def start_round(self):
        self.state = "round_start"
        return self.rounds_list[-1].start_round()

    def end_round(self):
        self.state = "end_start"
        self.rounds_list[-1].end_round()

    @property
    def serialized(self):
        tournament_dict = dict(self.__dict__)
        del tournament_dict["state"]
        del tournament_dict["matches_already_played_list"]

        tournament_dict["rounds_list"] = [round.serialized for round in self.rounds_list]

        tournament_dict["players_list"] = [player.id for player in self.players_list]

        return tournament_dict

    def last_round_analyze(self):

        if len(self.rounds_list) == self.rounds_number and self.is_round_end:
            self.state = "tournament_over"
            return "Il n'y a plus de rondes à jouer dans ce tournoi"

        elif not self.is_round_start:
            self.state = "round_not_start"
            return f"La ronde {self.rounds_list[-1].name} est à jouer"

        else:
            self.state = "round_start"
            return f"La ronde {self.rounds_list[-1].name} se joue actuellement"

    @property
    def is_round_start(self):
        if self.rounds_list[-1].start_time_round is None:
            return False
        return True

    @property
    def is_round_end(self):
        """a round is end if the end time is not None,
        and the end time is automatically fill when all the score are entered"""
        if self.rounds_list[-1].end_time_round is None:
            return False
        return True

    def ranking_players_after_round(self):
        players_dict = {}
        for round in self.rounds_list:
            for match in round.matches_list:
                player_one = match.match[0][0]
                player_two = match.match[1][0]
                result_one = match.match[0][1]
                result_two = match.match[1][1]
                if result_one is not None:
                    self.matches_already_played_list.append((player_one, player_two))
                    players_dict[player_one] = players_dict.get(player_one, 0) + result_one
                    players_dict[player_two] = players_dict.get(player_two, 0) + result_two
        ranked_players_list = []

        for key, value in players_dict.items():
            ranked_players_list.append((value, key.ranking, key))
        ranked_players_list.sort(key=lambda x: x[1])
        ranked_players_list.sort(key=lambda x: x[0], reverse=True)
        ranked_players_point_list = list(ranked_players_list)
        ranked_players_list = [player[2] for player in ranked_players_list]

        return ranked_players_list, ranked_players_point_list

    def following_round_generation(self):
        ranked_players_list, _ = self.ranking_players_after_round()
        players_pair_list = []
        while ranked_players_list:
            j = 1
            while (ranked_players_list[0], ranked_players_list[j],) in self.matches_already_played_list or (
                ranked_players_list[j],
                ranked_players_list[0],
            ) in self.matches_already_played_list:
                # match already played
                if j == len(ranked_players_list) - 1:
                    # no more possible combinations so we keep the first combinations
                    # that is the two strongest players in this tournament so far
                    j = 1
                    break
                j += 1
            players_pair_list.append((ranked_players_list[0], ranked_players_list[j]))
            ranked_players_list.remove(ranked_players_list[j])
            ranked_players_list.remove(ranked_players_list[0])

        self.rounds_list.append(
            Rounds(
                name="Round " + str(len(self.rounds_list) + 1),
                matches_list=players_pair_list,
            )
        )

    def first_round_generation(self):
        # sort the player list to generate the firt round
        players_list = [(player.ranking, player) for player in self.players_list]
        players_list.sort()
        players_list = [player for _, player in players_list]
        players_pair_list = []
        half_players_number = int(len(self.players_list) / 2)
        for i in range(half_players_number):
            players_pair_list.append((players_list[i], players_list[i + half_players_number]))

        self.rounds_list.append(
            Rounds(
                name="Round " + str(len(self.rounds_list) + 1),
                matches_list=players_pair_list,
            )
        )
