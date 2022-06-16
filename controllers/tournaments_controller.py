import re
from chess import DATE_REGEX
from views.tournament_view import TournamentView
from models.tournaments import Tournaments
from models.players import Players


class TournamentsController:
    """
    Manages user requests (through the tournament view)
    with the tournament model
    """

    def __init__(self, db, players_controller):
        self.tournament_view = TournamentView()
        self.db = db
        self.table = db.table("tournaments")
        self.players_number = 8
        self.rounds_number = 4
        self.id_selected_tournament = 0
        self.name_selected_tournament = ""
        self.id_tournaments_list = self.table_to_id()
        self.players_controller = players_controller
        self.tournament = None
        self.id_choice = None
        self.players_dict = None

    def display_tournaments_list(self, **args):
        table = self.db.load_all(self.table)
        self.tournament_view.clear_console()
        self.tournament_view.display_list(table, **args)

    def select_last_tournament(self):

        if self.id_tournaments_list:
            self.select_tournament(self.id_tournaments_list[-1])

    def table_to_id(self):
        return [record.doc_id for record in self.db.load_all(self.table)]

    def select_tournament(self, id_choice):
        """load in memory the selected tournament"""
        self.tournament = self.instantiation(id_choice)

    def instantiation(self, id_choice=None, tournament_dict=None):
        """
        we instantiate from the database or from
        a dictionary (after adding a tournament)
        """
        if not tournament_dict:
            tournament_dict = self.db.get_id(self.table, id_choice)
        # players are players objects in the list of the instance tournament
        tournament_dict["players_list"] = self.players_instantiation(tournament_dict["players_list"])
        # players are players objects in the rounds of the instance tournament
        tournament_dict["rounds_list"] = self.id_to_instance_player(tournament_dict["rounds_list"])

        tournament = Tournaments(**tournament_dict)
        self.id_tournaments_list = self.table_to_id()
        self.name_selected_tournament = tournament.name + " à " + tournament.location + " le " + tournament.date
        self.tournament_view.clear_console(self.name_selected_tournament)
        self.id_choice = id_choice
        return tournament

    def players_instantiation(self, players_list):
        # players_dict : keys are players id and values are players object
        self.players_dict = {}
        for id_player in players_list:
            self.players_dict[id_player] = Players(id=id_player, **self.id_player_to_dict_player(id_player))
        return list(self.players_dict.values())

    def id_player_to_dict_player(self, id_player):
        return self.db.get_id(self.players_controller.table, id_player)

    def id_to_instance_player(self, rounds_list):
        for round in rounds_list:
            for match in round["matches_list"]:
                match[0][0] = self.players_dict[match[0][0]]
                match[1][0] = self.players_dict[match[1][0]]
        return rounds_list

    def load_tournament(self):
        self.tournament_view.clear_console(self.name_selected_tournament)
        self.display_tournaments_list(id=True, display_name="tournaments_display")
        if self.id_tournaments_list:
            while True:
                id_choice = self.tournament_view.id_choice(self.id_tournaments_list)
                if id_choice in self.id_tournaments_list:
                    break
            self.select_tournament(id_choice)

    def add_tournament(self):
        while True:
            tournament_dict = self.tournament_view.input_tournament()
            tournament_dict["rounds_number"] = self.rounds_number
            tournament_dict["rounds_list"] = []
            id_players_list = self.players_controller.display_players_list(id=True, display_name="players_display")
            tournament_dict["players_list"] = self.tournament_view.input_tournament_players_list(
                id_players_list, self.players_number
            )
            if self.control_data_tournament(tournament_dict):
                break

        self.tournament = self.instantiation(tournament_dict=tournament_dict)
        # creation of the first round
        self.tournament.first_round_generation()
        self.id_choice = self.db.insert(self.table, self.tournament.serialized)

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

                first_player = match.match[0][0].last_name + " " + match.match[0][0].first_name
                second_player = match.match[1][0].last_name + " " + match.match[1][0].first_name
                result_first_player = str(match.match[0][1])
                result_second_player = str(match.match[1][1])  #
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

                else:  # to just create the list of the next round to play
                    if round_number == len(self.tournament.rounds_list) - 1:
                        matches_tournament_list.append(
                            {
                                "round_name": round.name,
                                "match": "(" + first_player + ", " + second_player + ")",
                            }
                        )

        self.tournament_view.display_list(matches_tournament_list, display_name=display_name, **args)

    def display_tournament_ranking_players_list(self, **args):
        _, ranked_players_point_list = self.tournament.ranking_players_after_round()
        display_list = []

        for rank, (point, ranking, player) in enumerate(ranked_players_point_list):
            display_list.append(
                {
                    "rank": rank + 1,
                    "score": float(point),
                    "name": player.last_name + " " + player.first_name,
                    "ranking": ranking,
                }
            )
        self.tournament_view.clear_console(self.name_selected_tournament)
        self.tournament_view.display_list(display_list, **args)

    def select_round(self):
        """
        select the last round to play (if it exists) or
        the round currently played of the selected tournament
        """

        self.tournament_view.clear_console(self.name_selected_tournament)
        self.tournament_view.message(self.tournament.last_round_analyze())
        if self.tournament.state == "tournament_over":
            return False

        elif self.tournament.state == "round_not_start":
            self.display_tournament_matches_list(display_name="matches_to_play_display")

        return True

    def start_round(self):
        self.tournament_view.clear_console(self.name_selected_tournament)
        if self.tournament.state == "round_not_start":
            # Record of the start time in round.start_time_round
            # Display of it
            self.tournament_view.message(self.tournament.start_round())
            # we save the tournament
            self.save()

        elif self.tournament.state == "round_start":
            self.tournament_view.message(f"La ronde {self.tournament.rounds_list[-1].name} est déjà démarrée")

    def end_round(self):
        if self.tournament.state == "round_start":
            self.tournament_view.message(
                "\nSaisie des résultats des matchs de la ronde (V = Victoire, E = Egalité, P = Perdu)\n"
            )
            round = self.tournament.rounds_list[-1]
            for match in round.matches_list:

                first_player = match.match[0][0].last_name + " " + match.match[0][0].first_name
                second_player = match.match[1][0].last_name + " " + match.match[1][0].first_name

                match_str = "(" + first_player + ", " + second_player + ")"
                while True:
                    score = self.tournament_view.input_result(first_player, match_str)
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

    def save(self):
        self.db.update_id(self.table, self.id_choice, self.tournament.serialized)

    def control_data_tournament(self, tournament):

        control = [
            isinstance(tournament["name"], str),
            isinstance(tournament["location"], str),
            re.match(DATE_REGEX, tournament["date"]),
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

        self.players_controller.player_view.display_list(players_tournament_list, order=order, **args)
