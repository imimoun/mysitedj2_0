from mysitedj2_0.utils import read_json_file

from scrabble.models.Deck import Deck
from scrabble.models.Game import Game
from scrabble.models.Player import Player


def init_token(id_deck):
    """ At the creation of the game, players take 7 cards from the deck """
    hand_player = []
    deck = Deck.objects.filter(id_deck=id_deck)
    seven_first_token = [object_token for object_token in deck[:7]]
    for object_token in seven_first_token:
        hand_player.append(object_token.token)
        object_token.delete()
    return hand_player


def create_deck(id_game):
    """ At the creation of the game, the deck is fill by tokens """
    tokens_to_create = read_json_file('scrabble/models/fixtures/init_deck_baby.json')
    id_deck = tokens_to_create[0]['fields']['id_deck']
    for token in tokens_to_create:
        new_token = Deck(id_token=token['id_token'],
                         id_deck=token['fields']['id_deck'],
                         token=token['fields']['token'])
        new_token.save()
    return id_deck


def get_game_or_create_it(id_game, id_player):
    """ If game exist, return id_game, else create it and return id_game """
    game_selected = Game.objects.filter(id_game=id_game)
    if len(game_selected) == 0:
        id_deck = create_deck(id_game)
        player_1 = Player.objects.get(id_player=id_player)
        hand_player_1 = init_token(id_deck)
        hand_player_2 = init_token(id_deck)
        game_selected = Game(id_game=id_game,
                             id_deck=id_deck,
                             player_1=player_1,
                             player_2=None,
                             hand_player_1=hand_player_1,
                             hand_player_2=hand_player_2)
        game_selected.save()
    return id_game


def token_played(post, name_input_begin_with, old_gameboard):
    """ Return list of token were not in old gameboard (with positions) """
    reponse = []

    for y in range(15):
        for x in range(15):
            value_token = post[name_input_begin_with + '_' + str(x) + '_' + str(y)]
            if old_gameboard[x][y] != value_token:
                reponse.append([post[name_input_begin_with + '_' + str(x) + '_' + str(y)], x, y])
    return reponse


def are_align_vertical(list_token):
    """ Return true if all token played are align in vertical """
    first_token = list_token[0]
    return len(list_token) == len([each for each in list_token if each[1] == first_token[1]])









#
