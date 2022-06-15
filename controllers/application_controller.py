from controllers.menu_controller import MenuController
from controllers.players_controller import PlayersController
from controllers.tournaments_controller import TournamentsController
from models.models import Models


class ApplicationsControllers:
    """
    Manages through menu, player and tournament controllers,the user's
    requests through his choices in the menus
    """

    def __init__(self):
        self.run()

    def run(self):
        self.main_menu = MenuController("main_menu")
        self.tournament_menu = MenuController("tournament_menu")
        self.round_menu = MenuController("round_menu")
        self.db = Models()
        self.players_controller = PlayersController(self.db)
        self.tournaments_controller = TournamentsController(self.db, self.players_controller)
        self.main_menu.view.clear_console()
        self.run_main_menu()

    def run_main_menu(self):
        while True:
            self.main_menu.display()
            if self.main_menu.choice == 1:
                self.players_controller.display_players_list(
                    order="ordre Alphabétique", display_name="players_display"
                )

            elif self.main_menu.choice == 2:
                self.players_controller.display_players_list(order="classement", display_name="players_display")

            elif self.main_menu.choice == 3:
                self.tournaments_controller.display_tournaments_list(display_name="tournaments_display")

            elif self.main_menu.choice == 4:
                self.players_controller.add_player()

            elif self.main_menu.choice == 5:
                self.players_controller.modify_player()

            elif self.main_menu.choice == 6:

                self.tournaments_controller.select_last_tournament()

                self.main_menu.view.clear_console(self.tournaments_controller.name_selected_tournament)
                self.run_tournament_menu()

            else:
                break

    def run_tournament_menu(self):

        while True:
            self.tournament_menu.display()
            if self.tournament_menu.choice == 1:
                self.tournaments_controller.load_tournament()

            elif self.tournament_menu.choice == 2:
                self.tournaments_controller.add_tournament()

            elif self.tournament_menu.choice == 3:
                self.tournaments_controller.display_tournament_players_list(
                    order="ordre Alphabétique", display_name="players_display"
                )

            elif self.tournament_menu.choice == 4:
                self.tournaments_controller.display_tournament_players_list(
                    order="classement", display_name="players_display"
                )

            elif self.tournament_menu.choice == 5:
                self.tournaments_controller.display_tournament_rounds_list(display_name="rounds_display")

            elif self.tournament_menu.choice == 6:
                self.tournaments_controller.display_tournament_matches_list(display_name="matches_display")

            elif self.tournament_menu.choice == 7:
                self.tournaments_controller.display_tournament_ranking_players_list(
                    display_name="tournament_ranking_display"
                )

            elif self.tournament_menu.choice == 8:

                if self.tournaments_controller.select_round():
                    self.run_round_menu()

            elif self.tournament_menu.choice == 9:
                self.tournament_menu.view.clear_console()
                break

    def run_round_menu(self):
        while True:
            self.round_menu.display()
            if self.round_menu.choice == 1:
                self.tournaments_controller.start_round()

            elif self.round_menu.choice == 2:
                self.tournaments_controller.end_round()
                break

            elif self.round_menu.choice == 3:
                self.tournament_menu.view.clear_console(self.tournaments_controller.name_selected_tournament)
                break
