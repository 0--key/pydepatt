#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
How to choose an arbitrary weapon
"""
from random import randrange


class Weapon(object):
    name = None
    cost = None

    @staticmethod
    def get_weapon(x):
        if x == 0:
            return Knife()
        if x == 1:
            return Gun()


class Knife(Weapon):
    name = 'Knife'
    cost = 20.00


class Gun(Weapon):
    name = 'Gun'
    cost = 300.00


# Create 5 random weapons
for _ in range(5):
    w = Weapon.get_weapon(randrange(2))
    print(w.name, w.cost)
