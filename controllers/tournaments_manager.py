from models.tournaments import Tournaments
from models.players_table import PlayersTable
from models.players import Players
from views.tournament_view import TournamentView
import tests.functions


class TournamentsManager:
    def __init__(self):
        self.tournament_view = TournamentView()

    def add_tournament(self, tournaments_table):
        tournament = self.tournament_view.input_tournament()
        tournaments_table.insert(tournament)

    def display_tournaments_list(self, tournaments_table):
        for e in tournaments_table.all():
            print(e)

        # self.tournament_view.display_tournaments_list


"""tournament = Tournaments(
    "tournament_1",
    "Bordeaux",
    "30/05/2022",
    "Nice day to play",
    "bullet",
)"""


# tests.functions.auto_add_players(tournament)
# tests.functions.auto_play_tournament(tournament)
