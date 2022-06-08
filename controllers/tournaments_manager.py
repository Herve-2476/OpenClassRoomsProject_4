from models.tournaments import Tournaments
from models.players_table import PlayersTable
from models.players import Players
from views.tournament_view_old import TournamentView
import tests.functions


class TournamentsManager:
    def __init__(self, table):
        self.tournament_view = TournamentView()
        self.table = table
        self.players_number = 8
        # table.truncate()
        # table.remove(doc_ids=[11])

    def add_tournament(self):
        self.tournament_dict = self.tournament_view.input_tournament()
        # self.tournament_dict = {}

    def display_tournaments_list(self):
        self.tournament_view.display_db_list(self.table.all())

    def add_tournament_players_list(self, id_players_list):
        self.tournament_dict[
            "players_list"
        ] = self.tournament_view.input_tournament_players_list(
            id_players_list, self.players_number
        )
        self.table.insert(self.tournament_dict)

    def last_tournament_record(self):
        return self.table.all()[-1]["players_list"]

    def matches_to_play_list(self):
        args = self.table.all()[-1]

        self.tournament = Tournaments(**args)
        tournament_players_list = []
        for player_id in self.tournament.players_list:
            args = self.players_table.get(doc_id=player_id)
            tournament_players_list.append(Players(**args))
        self.tournament.players_list = list(tournament_players_list)

        self.tournament.first_round_generation()

        for p1, p2 in self.tournament.rounds_list[-1].players_pair_list:
            print(p1.last_name, p2.last_name)

    def recording_round_results(self):
        tests.functions.play_round_new(self.tournament)


"""tournament = Tournaments(
    "tournament_1",
    "Bordeaux",
    "30/05/2022",
    "Nice day to play",
    "bullet",
)"""


# tests.functions.auto_add_players(tournament)
# tests.functions.auto_play_tournament(tournament)
