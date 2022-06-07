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
        tournaments_controller = TournamentsController(db)
        main_menu.view.clear_console()
        while True:
            main_menu.display()
            if main_menu.choice == 1:
                players_controller.display_players_list(order="ordre Alphabétique")

            elif main_menu.choice == 2:
                players_controller.display_players_list(order="classement")

            elif main_menu.choice == 3:
                tournaments_controller.display_tournaments_list()

            elif main_menu.choice == 6:
                main_menu.view.clear_console()
                tournament_menu.display()
                while True:
                    if tournament_menu.choice == 9:
                        tournament_menu.view.clear_console()
                        break
            else:
                break
