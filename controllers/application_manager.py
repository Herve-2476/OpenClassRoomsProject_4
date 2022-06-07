import os

from models.models import Models

# import controllers.tournament_manager
from tinydb import TinyDB
import tests.functions
from controllers.players_manager import PlayersManager
from controllers.players_manager import PlayersManagerNew
from controllers.tournaments_manager import TournamentsManager
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from controllers.menu_manager import MenuManager


clearConsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


db = Models()
players_table = db.table("players")
player_view = PlayerView()
players_manager = PlayersManager()
players_manager_new = PlayersManagerNew(db.table("players"))
tournaments_manager = TournamentsManager(db.table("tournaments"))
tournaments_manager.players_table = players_manager_new.table


main_menu = MenuManager("main_menu")
main_menu.view.clear_console()
while True:
    main_menu.display()
    if main_menu.choice == 1:

        main_menu.view.clear_console()
        players_list, correspondence_players_dict = players_manager.load_players_list(
            players_table
        )
        player_view.display_players_list(
            players_manager.sort_in_alphabetical_order(players_list),
        )

    elif main_menu.choice == 2:
        main_menu.view.clear_console()
        players_list, correspondence_players_dict = players_manager.load_players_list(
            players_table
        )
        player_view.display_players_list(
            players_manager.sort_in_ranking_order(players_list),
        )
    elif main_menu.choice == 3:
        tournaments_manager.display_tournaments_list()

    elif main_menu.choice == 4:
        main_menu.view.clear_console()
        players_manager.add_player(players_table)
        main_menu.view.clear_console()

    elif main_menu.choice == 5:
        main_menu.view.clear_console()
        players_list, correspondence_players_dict = players_manager.load_players_list(
            players_table
        )

        player_view.display_players_list(
            players_manager.sort_in_alphabetical_order(players_list),
            correspondence_players_dict,
        )

        players_manager.modify_data_player(players_table, correspondence_players_dict)
        main_menu.view.clear_console()

    elif main_menu.choice == 6:
        tournaments_manager.add_tournament()
        id_players_list = players_manager_new.display_players_list()
        tournaments_manager.add_tournament_players_list(id_players_list)

    elif main_menu.choice == 7:
        tournaments_manager.matches_to_play_list()

    elif main_menu.choice == 8:
        tournaments_manager.recording_round_results()

    else:
        break


# tests.functions.data_players_creation(players_table)

# players_table.remove(doc_ids=[12])
