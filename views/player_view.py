class PlayerView:
    def display_line(self, line):
        form = "{0:15}{1:15}{2:15}{3:8}{4:4}"
        print(form.format(*line))

    def display_players_list(self, players_list):
        if players_list:
            self.display_line(players_list[0].__dict__.keys())
            print()
            for player in players_list:
                self.display_line(player.__dict__.values())
