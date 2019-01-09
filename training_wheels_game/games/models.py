# -*- coding: utf-8 -*-
from django.db import models


class ListOfGames(models.Model):
    Game_title = models.TextField(verbose_name="Game Title")
    Players = models.TextField(verbose_name="Players")
    To_game = models.TextField()
