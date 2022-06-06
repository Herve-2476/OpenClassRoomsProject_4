from models.tournaments import Tournaments
from models.players_table import PlayersTable
from models.players import Players
from views.tournament_view import TournamentView
import tests.functions


class TournamentsManager:
    def __init__(self, table):
        self.tournament_view = TournamentView()
        self.table = table
        self.players_number = 8
        # table.truncate()

    def add_tournament(self):
        # self.tournament_dict = self.tournament_view.input_tournament()
        self.tournament_dict = {}

    def display_tournaments_list(self):
        self.tournament_view.display_db_list(self.table.all())

    def add_tournament_players_list(self, id_players_list):
        print(id_players_list)
        self.tournament_dict[
            "players_list"
        ] = self.tournament_view.input_tournament_players_list(
            id_players_list, self.players_number
        )
        self.table.insert(self.tournament)


"""tournament = Tournaments(
    "tournament_1",
    "Bordeaux",
    "30/05/2022",
    "Nice day to play",
    "bullet",
)"""


# tests.functions.auto_add_players(tournament)
# tests.functions.auto_play_tournament(tournament)
