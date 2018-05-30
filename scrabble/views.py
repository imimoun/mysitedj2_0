from django.shortcuts import redirect, render

from scrabble.models.Player import Player


def index(request):
    """ User choose his id_player and a id_gameboard to play. """
    list_all_player = Player.objects.all()
    if request.POST and request.POST["id_player"] and request.POST["id_gameboard"]:
        id_player = request.POST["id_player"]
        id_gameboard = request.POST["id_gameboard"]

        return redirect('gameboard',
                        id_gameboard=id_gameboard,
                        id_player=id_player)

    return render(request, 'scrabble-login.html', {
        'list_all_player': list_all_player
    })


def gameboard(request, id_gameboard, id_player):
    """ Check if ids exist. Create and init gameboard if it doesn't. """
    return render(request, 'gameboard.html')
