from controllers.menu_controller import MenuController
from controllers.players_controller import PlayersController
from controllers.tournaments_controller import TournamentsController
from models.models import Models


class ApplicationsControllers:
    def __init__(self):
        self.run()

    def run(self):
        main_menu = MenuController("main_menu")
        tournament_menu = MenuController("tournament_menu")
        db = Models()
        players_controller = PlayersController(db)
        tournaments_controller = TournamentsController(db, players_controller)
        main_menu.view.clear_console()
        while True:
            main_menu.display()
            if main_menu.choice == 1:
                players_controller.display_players_list(
                    id=False, order="ordre Alphabétique"
                )

            elif main_menu.choice == 2:
                players_controller.display_players_list(id=False, order="classement")

            elif main_menu.choice == 3:
                tournaments_controller.display_tournaments_list()

            elif main_menu.choice == 4:
                players_controller.add_player()

            elif main_menu.choice == 5:
                players_controller.modify_player()

            elif main_menu.choice == 6:
                main_menu.view.clear_console(
                    tournaments_controller.name_selected_tournament
                )

                while True:
                    tournament_menu.display()
                    if tournament_menu.choice == 1:
                        tournaments_controller.load_tournament()

                    elif tournament_menu.choice == 2:
                        tournaments_controller.add_tournament()

                    elif tournament_menu.choice == 9:
                        tournament_menu.view.clear_console()
                        break
            else:
                break
