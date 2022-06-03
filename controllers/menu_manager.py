import views.menu_view


class MenuManager:
    menu_dict = {
        "main_menu": [
            "Liste de tous les joueurs par ordre alphabétique",
            "Liste de tous les joueurs par ordre de classement",
            "Liste de tous les tournois",
            "Quitter le programme",
        ]
    }

    def __init__(self, menu):
        self.view = views.menu_view.Menu(self.menu_dict["main_menu"])

    def display(self):
        self.choice = self.view.display_menu()
