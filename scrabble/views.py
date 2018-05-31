from django.shortcuts import redirect, render

from scrabble.models.Player import Player


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
    return render(request, 'gameboard.html')
