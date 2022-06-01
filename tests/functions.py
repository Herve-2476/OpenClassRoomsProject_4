import random

from models.players import Players
from models import data
from controllers.players_manager import PlayersManager


def data_players_creation(players_table):
    index_list_players = range(len(data.players))
    rank_players_list = players_instantiation(index_list_players)
    rank_players_list = [player.serialized_player() for _, player in rank_players_list]
    players_table.truncate()
    players_table.insert_multiple(rank_players_list)


def auto_add_players(tournament):
    index_list_players = random.sample(range(len(data.players)), 8)
    # index_list_players = range(len(data.players))
    rank_players_list = players_instantiation(index_list_players)

    for _, player in sorted(rank_players_list):
        tournament.add_player(player)


def players_instantiation(index_list_players):
    rank_players_list = []
    for index_player in index_list_players:
        ranking = data.players[index_player]["ranking"]
        rank_players_list.append(
            (
                ranking,
                Players(
                    last_name=data.players[index_player]["last_name"],
                    first_name=data.players[index_player]["first_name"],
                    birthday_date=data.players[index_player]["birthday_date"],
                    gender=data.players[index_player]["gender"],
                    ranking=data.players[index_player]["ranking"],
                ),
            )
        )
    return rank_players_list


def auto_play_tournament(tournament):
    tournament.first_round_generation()
    play_round(tournament)
    while len(tournament.rounds_list) < tournament.rounds_number:

        (
            ranked_players_list,
            matches_list,
            ranked_players_point_list,
        ) = tournament.ranking_players_after_round()
        tournament.score_display(ranked_players_point_list)
        tournament.following_round_generation(ranked_players_list, matches_list)
        play_round(tournament)

    # break
    _, _, ranked_players_point_list = tournament.ranking_players_after_round()
    tournament.score_display(ranked_players_point_list)


def play_round(tournament):
    round = tournament.rounds_list[-1]
    round.input_results(auto_round_result(len(round.players_pair_list)))
    round.end_round()

    for match in round.matches_list:
        player_one = match.match[0][0]
        player_two = match.match[1][0]
        result_player_one = match.match[0][1]
        result_player_two = match.match[1][1]
        print(
            f"résultat du match {player_one.last_name} , {player_two.last_name} = {result_player_one} , {result_player_two}"
        )


def auto_round_result(n):
    result_list = []
    for i in range(n):
        result = random.randint(0, 2)
        if result == 0:
            result_list.append((1, 0))
        elif result == 1:
            result_list.append((0.5, 0.5))
        else:
            result_list.append((0, 1))
    return result_list
