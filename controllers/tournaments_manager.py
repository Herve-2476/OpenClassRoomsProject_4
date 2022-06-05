from models.tournaments import Tournaments
from models.players_table import PlayersTable
from models.players import Players
from views.tournament_view import TournamentView
import tests.functions


class TournamentsManager:
    def __init__(self, table):
        self.tournament_view = TournamentView()
        self.table = table
        table.truncate()

    def add_tournament(self):
        tournament = self.tournament_view.input_tournament()
        self.table.insert(tournament)

    def display_tournaments_list(self):
        self.tournament_view.display_db_list(self.table.all())


"""tournament = Tournaments(
    "tournament_1",
    "Bordeaux",
    "30/05/2022",
    "Nice day to play",
    "bullet",
)"""


# tests.functions.auto_add_players(tournament)
# tests.functions.auto_play_tournament(tournament)
