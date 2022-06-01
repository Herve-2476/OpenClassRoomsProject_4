# import controllers.tournament_manager

from controllers.players_manager import PlayersManager
from views.player_view import PlayerView


class ApplicationManager:
    def players_manager(self):
        return PlayersManager()


manager = ApplicationManager()
player_view = PlayerView()
players_manager = manager.players_manager()
players_list = players_manager.load_players_list()
player_view.display_players_list(
    players_manager.sort_in_alphabetical_order(players_list)
)
player_view.display_players_list(players_manager.sort_in_ranking_order(players_list))
