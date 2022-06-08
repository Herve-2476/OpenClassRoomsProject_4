import views.menu_view


class MenuController:
    menu_dict = {
        "main_menu": [
            "Liste de tous les joueurs par ordre alphabétique",
            "Liste de tous les joueurs par classement",
            "Liste de tous les tournois",
            "Entrer un nouveau joueur",
            "Modifier un joueur",
            "Menu tournoi",
            "Quitter",
        ],
        "tournament_menu": [
            "Charger un tournoi",
            "Créer un tournoi",
            "Liste des matchs à jouer",
            "Enregistrer les résultats de la ronde",
            "Liste de tous les joueurs du tournoi par ordre alphabétique",
            "Liste de tous les joueurs du tournoi par classement",
            "Liste de tous les tours d'un tournoi",
            "Liste de tous les matchs d'un tournoi",
            "Menu principal",
        ],
    }

    def __init__(self, menu):
        self.menu_list = self.menu_dict[menu]
        self.view = views.menu_view.Menu(self.menu_list)

    def display(self):
        while True:
            self.choice = self.view.display_menu()
            try:
                if 1 <= self.choice <= len(self.menu_list):
                    break
            except:
                pass
