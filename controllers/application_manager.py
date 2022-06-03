import os

# import controllers.tournament_manager
from tinydb import TinyDB
import tests.functions
from controllers.players_manager import PlayersManager
from controllers.tournaments_manager import TournamentsManager
from views.player_view import PlayerView
from controllers.menu_manager import MenuManager


clearConsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


db = TinyDB("db.json")
players_table = db.table("players")
tournaments_table = db.table("tournaments")
player_view = PlayerView()
players_manager = PlayersManager()
tournaments_manager = TournamentsManager()


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
        tournaments_manager.display_tournaments_list(tournaments_table)

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
        tournaments_manager.add_tournament(tournaments_table)

    else:
        break


# tests.functions.data_players_creation(players_table)

# players_table.remove(doc_ids=[12])
