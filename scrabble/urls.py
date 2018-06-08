from django.urls import path

from scrabble import views

urlpatterns = [
    path('gameboard/<int:id_game>/<int:id_player>', views.gameboard, name='gameboard'),
    path('gameboard/<int:id_game>/<int:id_player>/user_play_turn', views.user_play_turn, name='user-play-turn'),
    path('', views.index, name='index-scrabble'),
]
