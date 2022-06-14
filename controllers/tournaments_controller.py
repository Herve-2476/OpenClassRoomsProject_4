import re
from views.tournament_view import TournamentView
from models.tournaments import Tournaments
from models.rounds import Rounds
from models.matches import Matches
from models.players import Players

# import random


class TournamentsController:
    def __init__(self, db, players_controller):
        self.tournament_view = TournamentView()
        self.db = db
        self.table = db.table("tournaments")
        self.players_number = 8
        self.rounds_number = 4
        self.id_selected_tournament = 0
        self.name_selected_tournament = ""
        self.players_controller = players_controller
        self.date_regex = (
            r"(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1\d|0[1-9]|1[012])\/(19|20)\d\d"
        )
        self.tournament = None

        # self.table.truncate()
        # for i in range(6, 11):
        # self.table.remove(doc_ids=[i])

    def display_tournament_ranking_players_list(self, **args):
        _, ranked_players_point_list = self.tournament.ranking_players_after_round()
        display_list = []

        for point, ranking, player in ranked_players_point_list:
            display_list.append(
                {
                    "score": float(point),
                    "name": player.last_name + " " + player.first_name,
                    "ranking": ranking,
                }
            )
        self.tournament_view.clear_console(self.name_selected_tournament)
        self.tournament_view.display_list(display_list, **args)

    def players_instantiation(self, players_list):
        self.players_dict = {}
        print(players_list)
        for id_player in players_list:
            self.players_dict[id_player] = Players(
                id=id_player, **self.id_player_to_dict_player(id_player)
            )
        return list(self.players_dict.values())

    def control_tournament_selection(self):
        """Menu Tournament = if no tournament selected, the last input tournament
        is selected if it exists"""

        if self.tournament is None:
            id_tournaments_list = self.display_tournaments_list(
                display_name="tournaments_display"
            )
            if id_tournaments_list:
                self.select_tournament(id_tournaments_list[-1])

    def display_tournaments_list(self, **args):
        table = self.db.load_all(self.table)
        self.tournament_view.display_db_list(table, **args)
        return [record.doc_id for record in table]

    def load_tournament(self):
        self.tournament_view.clear_console(self.name_selected_tournament)
        id_tournaments_list = self.display_tournaments_list(
            display_name="tournaments_display"
        )
        if id_tournaments_list:
            while True:
                id_choice = self.tournament_view.id_choice(id_tournaments_list)
                if id_choice in id_tournaments_list:
                    break
            self.select_tournament(id_choice)

    def select_tournament(self, id_choice):
        self.tournament = self.instantiation(id_choice)

    def id_to_instance_player(self, rounds_list):
        for round in rounds_list:
            for match in round["matches_list"]:
                match[0][0] = self.players_dict[match[0][0]]
                match[1][0] = self.players_dict[match[1][0]]
        return rounds_list

    def instantiation(self, id_choice=None, tournament_dict=None):
        if not tournament_dict:
            tournament_dict = self.db.get_id(self.table, id_choice)

        # id_players to object_players
        tournament_dict["players_list"] = self.players_instantiation(
            tournament_dict["players_list"]
        )

        tournament_dict["rounds_list"] = self.id_to_instance_player(
            tournament_dict["rounds_list"]
        )

        tournament = Tournaments(**tournament_dict)

        tournament.rounds_list = [Rounds(**round) for round in tournament.rounds_list]

        if False:
            print(tournament.rounds_list)

            for round in tournament.rounds_list:
                print(round.matches_list[0].match)
                round.matches_list = [Matches(**match) for match in round.matches_list]
                if False:
                    for match in round.matches_list:
                        match[0][0] = Players(
                            **self.id_player_to_dict_player(match[0][0])
                        )
                        match[1][0] = Players(
                            **self.id_player_to_dict_player(match[1][0])
                        )
        self.name_selected_tournament = (
            tournament.name + " à " + tournament.location + " le " + tournament.date
        )
        self.tournament_view.clear_console(self.name_selected_tournament)
        self.id_choice = id_choice
        return tournament

    def id_player_to_dict_player(self, id_player):
        return self.db.get_id(self.players_controller.table, id_player)

    def add_tournament(self):
        while True:
            tournament_dict = self.tournament_view.input_tournament()
            tournament_dict["rounds_number"] = self.rounds_number
            tournament_dict["rounds_list"] = []
            id_players_list = self.players_controller.display_players_list(
                display_name="players_display"
            )
            tournament_dict[
                "players_list"
            ] = self.tournament_view.input_tournament_players_list(
                id_players_list, self.players_number
            )
            if self.control_data_tournament(tournament_dict):
                break
        """
        tournament_dict = {
            "name": "tournoi_7",
            "location": "bordeaux",
            "date": "01/01/2022",
            "players_list": [1, 15, 3, 4, 6, 7, 8, 9],
            "description": "It's cloudy",
            "time_control": "bullet",
            "rounds_number": 4,
            "rounds_list": [],
        }
        """
        self.tournament = self.instantiation(tournament_dict=tournament_dict)
        self.tournament.first_round_generation()
        self.db.insert(self.table, self.tournament.serialized)

    def save(self):

        self.db.update_id(self.table, self.id_choice, self.tournament.serialized)

    def control_data_tournament(self, tournament):

        control = [
            isinstance(tournament["name"], str),
            isinstance(tournament["location"], str),
            re.match(self.date_regex, tournament["date"]),
            tournament["time_control"] in ["bullet", "blitz", "coup rapide"],
            isinstance(tournament["description"], str),
        ]
        return all(control)

    def display_tournament_players_list(self, order, **args):
        self.tournament_view.clear_console(self.name_selected_tournament)
        players_tournament_list = []
        for player in self.tournament.players_list:
            players_tournament_list.append(player.serialized_player())

        players_tournament_list.sort(key=lambda x: x["ranking"])
        if order == "ordre Alphabétique":
            players_tournament_list.sort(key=lambda x: x["first_name"])
            players_tournament_list.sort(key=lambda x: x["last_name"])

        self.players_controller.player_view.display_list(
            players_tournament_list, order=order, **args
        )

    def display_tournament_rounds_list(self, **args):
        self.tournament_view.clear_console(self.name_selected_tournament)
        rounds_tournament_list = []
        for round in self.tournament.rounds_list:
            rounds_tournament_list.append(round.serialized)
        self.tournament_view.display_list(rounds_tournament_list, **args)

    def display_tournament_matches_list(self, display_name="", **args):
        self.tournament_view.clear_console(self.name_selected_tournament)
        matches_tournament_list = []
        for round_number, round in enumerate(self.tournament.rounds_list):

            for match in round.matches_list:

                first_player = (
                    match.match[0][0].last_name + " " + match.match[0][0].first_name
                )
                second_player = (
                    match.match[1][0].last_name + " " + match.match[1][0].first_name
                )
                result_first_player = str(match.match[0][1])
                result_second_player = str(match.match[1][1])
                if display_name == "matches_display":
                    matches_tournament_list.append(
                        {
                            "round_name": round.name,
                            "first_player": first_player,
                            "result_first_player": result_first_player,
                            "second_player": second_player,
                            "result_second_player": result_second_player,
                        }
                    )

                else:
                    if round_number == len(self.tournament.rounds_list) - 1:
                        matches_tournament_list.append(
                            {
                                "round_name": round.name,
                                "match": "("
                                + first_player
                                + ", "
                                + second_player
                                + ")",
                            }
                        )

        self.tournament_view.display_list(
            matches_tournament_list, display_name=display_name, **args
        )

    def control_round_selection(self):
        """select the last round to play (if it exist) of the selected tournament"""
        self.tournament_view.clear_console(self.name_selected_tournament)
        self.tournament_view.message(self.tournament.last_round_analyze())
        if self.tournament.state == "tournament_over":
            return False

        elif self.tournament.state == "round_not_start":
            self.display_tournament_matches_list(display_name="matches_to_play_display")

        elif self.tournament.state == "round_start":
            pass

        elif self.tournament.state == "round_end":
            pass
        return True

    def start_round(self):
        self.tournament_view.clear_console(self.name_selected_tournament)
        if self.tournament.state == "round_not_start":
            self.tournament_view.message(self.tournament.start_round())
            self.tournament.state = "round_start"
            self.save()

        elif self.tournament.state == "round_start":
            self.tournament_view.message(
                f"La ronde {self.tournament.rounds_list[-1].name} est déjà démarrée"
            )

    def end_round(self):
        if self.tournament.state == "round_start":
            self.tournament_view.message(
                "\nSaisie des résultats des matchs de la ronde (V = Victoire, E = Egalité, P = Perdu)\n"
            )
            round = self.tournament.rounds_list[-1]
            for match in round.matches_list:

                first_player = (
                    match.match[0][0].last_name + " " + match.match[0][0].first_name
                )
                second_player = (
                    match.match[1][0].last_name + " " + match.match[1][0].first_name
                )

                match_str = "(" + first_player + ", " + second_player + ")"
                while True:
                    score = self.tournament_view.input_result(first_player, match_str)
                    # score = ["V", "E", "P"][random.randint(0, 2)]
                    if score in [
                        "V",
                        "E",
                        "P",
                    ]:
                        break
                self.tournament.record_match(match, score)

            self.tournament.end_round()
            if len(self.tournament.rounds_list) < self.tournament.rounds_number:
                self.tournament.following_round_generation()
            self.save()
            self.tournament_view.clear_console(self.name_selected_tournament)

        else:
            self.tournament_view.clear_console(self.name_selected_tournament)
            self.tournament_view.message("La ronde n'est pas démarrée...")
