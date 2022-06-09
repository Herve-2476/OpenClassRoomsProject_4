import re
from views.tournament_view import TournamentView
from models.tournaments import Tournaments
from models.rounds import Rounds
from models.matches import Matches
from models.players import Players


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
            "(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1\d|0[1-9]|1[012])\/(19|20)\d\d"
        )
        self.tournament = None

        # self.table.truncate()
        # table.remove(doc_ids=[11])

    def control_round_selection(self):
        """select the last round to play (if it exist) of the selected tournament"""
        self.tournament.last_round_analyze()

    def control_tournament_selection(self):
        """if no tournament selected, the last input tournament is selected if it exist"""
        if not self.tournament:
            id_tournaments_list = self.display_tournaments_list()
            if id_tournaments_list:
                self.select_tournament(id_tournaments_list[-1])

    def display_tournaments_list(self, **args):
        table = self.db.load_all(self.table)
        self.tournament_view.display_db_list(table, **args)
        return [record.doc_id for record in table]

    def load_tournament(self):
        self.tournament_view.clear_console(self.name_selected_tournament)
        id_tournaments_list = self.display_tournaments_list()
        if id_tournaments_list:
            while True:
                id_choice = self.tournament_view.id_choice(id_tournaments_list)
                if id_choice in id_tournaments_list:
                    break
            self.select_tournament(id_choice)

    def select_tournament(self, id_choice):
        self.tournament = self.instantiation(id_choice)
        self.name_selected_tournament = (
            self.tournament.name
            + " à "
            + self.tournament.location
            + " le "
            + self.tournament.date
        )
        self.tournament_view.clear_console(self.name_selected_tournament)

    def instantiation(self, id_choice=None, tournament_dict=None):
        if not tournament_dict:
            tournament_dict = self.db.get_id(self.table, id_choice)
        tournament = Tournaments(**tournament_dict)

        tournament.rounds_list = [Rounds(**round) for round in tournament.rounds_list]
        for round in tournament.rounds_list:
            round.matches_list = [Matches(**match) for match in round.matches_list]
            for match in round.matches_list:
                match[0][0] = Players(**self.id_player_to_dict_player(match[0][0]))
                match[1][0] = Players(**self.id_player_to_dict_player(match[1][0]))
        return tournament

    def id_player_to_dict_player(self, id_player):
        return self.db.get_id(self.players_controller.table, id_player)

    def add_tournament(self):
        while False:
            tournament = self.tournament_view.input_tournament()
            tournament["rounds_number"] = self.rounds_number
            tournament["rounds_list"] = [{"name": "Round 1"}]
            id_players_list = self.players_controller.display_players_list()
            tournament[
                "players_list"
            ] = self.tournament_view.input_tournament_players_list(
                id_players_list, self.players_number
            )
            if self.control_data_tournament(tournament):
                break

        tournament = {
            "name": "tournoi_4",
            "location": "bordeaux",
            "date": "01/01/2022",
            "players_list": [1, 2, 3, 4, 6, 7, 8, 9],
            "description": "Nice day to play",
            "time_control": "bullet",
            "rounds_number": 4,
            "rounds_list": [],
        }

        self.tournament = self.instantiation(tournament_dict=tournament)
        print(self.tournament.__dict__)

        self.tournament.first_round_generation()
        self.tournament.rounds_list[-1].display()

        assert 1 == 2

        self.select_tournament(self.db.insert(self.table, tournament))

    def control_data_tournament(self, tournament):
        control = [
            isinstance(tournament["name"], str),
            isinstance(tournament["location"], str),
            re.match(self.date_regex, tournament["date"]),
            tournament["time_control"] in ["bullet", "blitz", "coup rapide"],
            isinstance(tournament["description"], str),
        ]
        return all(control)
