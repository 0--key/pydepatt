#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An attempt to illustrate how pet_factory works
"""
import unittest
from pet_factory import Dog, Cat, spawn_pet


class TestPetBehavior(unittest.TestCase):

    def setUp(self):
        self.D = Dog('Hound')

    def test_dog_init_name(self):
        self.assertEqual(self.D._name, 'Hound')

    def test_dog_speak_ability(self):
        self.assertEqual(self.D.speak(), 'Woof!')
