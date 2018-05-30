from django.urls import path

from scrabble import views

urlpatterns = [
    path('gameboard/<int:id_gameboard>/<int:id_player>', views.gameboard, name='gameboard'),
    path('', views.index, name='index-scrabble'),
]
