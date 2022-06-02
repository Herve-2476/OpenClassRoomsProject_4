import views.menu_view


class MenuManager:
    menu_dict = {
        "main_menu": [
            "Liste de tous les joueurs par ordre alphabétique",
            "Liste de tous les joueurs par ordre de classement",
            "Liste de tous les tournois",
        ]
    }

    def __init__(self, menu):
        self.menu_list = self.menu_dict[menu]

    def display(self):
        self.choice = views.menu_view.Menu().display_menu(self.menu_list)
