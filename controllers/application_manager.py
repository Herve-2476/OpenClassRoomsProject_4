# import controllers.tournament_manager
from tinydb import TinyDB
import tests.functions
from controllers.players_manager import PlayersManager
from views.player_view import PlayerView
from models.players_table import PlayersTable


class ApplicationManager:
    def players_manager(self):
        return PlayersManager()


# tests.functions.data_players_creation(PlayersTable())

players_list = None
manager = ApplicationManager()
player_view = PlayerView()
players_manager = manager.players_manager()
players_list = players_manager.load_players_list()
player_view.display_players_list(
    players_manager.sort_in_alphabetical_order(players_list)
)
player_view.display_players_list(players_manager.sort_in_ranking_order(players_list))

# players_manager.add_player()
players_list = players_manager.load_players_list()
player_view.display_players_list(players_manager.sort_in_ranking_order(players_list))
