# import controllers.tournament_manager
from tinydb import TinyDB
import tests.functions
from controllers.players_manager import PlayersManager
from views.player_view import PlayerView
from models.players_table import PlayersTable


db = TinyDB("db.json")
players_table = db.table("players")

# tests.functions.data_players_creation(players_table)

# players_table.remove(doc_ids=[12])
if True:
    player_view = PlayerView()
    players_manager = PlayersManager()
    players_list, correspondence_players_dict = players_manager.load_players_list(
        players_table
    )

    player_view.display_players_list(
        players_manager.sort_in_alphabetical_order(players_list)
    )
    player_view.display_players_list(
        players_manager.sort_in_ranking_order(players_list), correspondence_players_dict
    )
    # players_table.remove(doc_ids=[5])
    players_manager.add_player(players_table)
    # players_manager.modify_data_player(players_table, correspondence_players_dict)
    players_list, correspondence_players_dict = players_manager.load_players_list(
        players_table
    )
    player_view.display_players_list(
        players_manager.sort_in_ranking_order(players_list), correspondence_players_dict
    )
