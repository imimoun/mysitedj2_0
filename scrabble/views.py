from django.shortcuts import redirect, render

from scrabble.models.Game import Game
from scrabble.models.Player import Player
from scrabble.utils import get_game_or_create_it


def index(request):
    """ User choose his id_player and a id_game to play. """
    list_all_player = Player.objects.all()
    if request.POST and request.POST["id_player"] and request.POST["id_game"]:
        id_player = request.POST["id_player"]
        id_game = request.POST["id_game"]

        return redirect('gameboard',
                        id_game=id_game,
                        id_player=id_player)

    return render(request, 'scrabble-login.html', {
        'list_all_player': list_all_player
    })


def gameboard(request, id_game, id_player):
    """ Check if ids exist. Create and init gameboard if it doesn't. """
    id_game = get_game_or_create_it(id_game, id_player)
    game = Game.objects.get(id_game=id_game)
    # import pdb; pdb.set_trace()
    return render(request, 'gameboard.html', {
        "game": game,
        "current_id_player": id_player
    })


def user_play_turn(request, id_game, id_player):
    """ A player play an valide. Check the word. Save on database. Redirect to gameboard. """
    game = Game.objects.get(id_game=id_game)
    # Check tokens played was in hand else raise error
    # token_proposed_by_player = token_proposed(id_game, id_player)
    # tokens_are_align_horizontal = are_align_horizontal(token_proposed_by_player)
    # tokens_are_align_vertical = are_align_vertical(token_proposed_by_player)
    #
    # if (tokens_are_align_horizontal or tokens_are_align_vertical):
    #     raise 'tokens propose are not align'
    #
    # old_token_before_new = tokens_before(game.gameboard,
    #                                      token_proposed_by_player,
    #                                      tokens_are_align_horizontal,
    #                                      tokens_are_align_vertical)
    #
    # old_token_between_new = tokens_before(game.gameboard,
    #                                       token_proposed_by_player,
    #                                       tokens_are_align_horizontal,
    #                                       tokens_are_align_vertical)
    #
    # old_token_after_new = tokens_before(game.gameboard,
    #                                     token_proposed_by_player,
    #                                     tokens_are_align_horizontal,
    #                                     tokens_are_align_vertical)
    #
    # word_proposed_as_list = sort(old_token_before_new +
    #                              old_token_between_new +
    #                              token_proposed_by_player +
    #                              old_token_after_new)
    #
    # word_proposed = [each[0] for each in word_proposed_as_list]
    #
    # if(word_proposed in ['enfant', 'bebe', 'maman']):
    #     # Update gameboard
    #     # Fill current hand


    return render(request, 'gameboard.html', {
        "game": game,
        "current_id_player": id_player
    })
