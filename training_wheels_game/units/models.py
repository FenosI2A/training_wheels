from django.db import models


class Unit (models.Model):
    TYPE_OF_UNIT = (
        ('R', 'Ranged'),
        ('M', 'Meele'),
        ('C', 'Cavalery'),
        ('RC', 'Ranged Cavalery')
    )
    unit_name = models.TextField()
    melee_attack = models.IntegerField()
    range_attack = models.IntegerField()
    range_distance = models.IntegerField()
    morale = models.IntegerField()
    movement_points = models.IntegerField()
    armored = models.BooleanField()
    armor_piercing = models.BooleanField()
    heavy_armored = models.BooleanField()
    firearm = models.BooleanField()
    cavalry = models.BooleanField()
    polearms = models.BooleanField()


class Terrain (models.Model):
    TYPE_OF_TERRAIN = (
        ('P', 'Plain'),
        ('F', 'Forest'),
        ('W', 'Water')
    )
