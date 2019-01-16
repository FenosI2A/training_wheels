# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Games(models.Model):
    game_title = models.CharField(max_length=100, null=False)
    player_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_is_host')
    player_2 = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='_is_Guest')
    game_state = models.TextField()
    active_player = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='_is_active')
