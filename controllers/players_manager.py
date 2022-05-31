from models.players_table import PlayersTable
from models.players import Players
import tests.functions


# tests.functions.data_players_creation(PlayersTable())
l = PlayersTable().load()
print(l)
