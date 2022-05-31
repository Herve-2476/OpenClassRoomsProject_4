from models.tournaments import Tournaments
from models.players import Players
from models.players_table import PlayersTable
import tests.functions


tournament = Tournaments(
    "tournament_1",
    "Bordeaux",
    "30/05/2022",
    "Nice day to play",
    "bullet",
)

tests.functions.auto_add_players(tournament)
tests.functions.auto_play_tournament(tournament)
