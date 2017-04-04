#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An attempt to illustrate how pet_factory works
"""
import unittest
from sophisticated_pet_factory import Dog, Cat, PetFactory


class TestPetBehavior(unittest.TestCase):

    def setUp(self):
        self.pet_factory = PetFactory()
        # self.cat = PetFactory('Cat')

    def test_dog_speak_ability(self):
        self.assertEqual(self.pet_factory.make_clamor('Dog'), 'Bhow Bhow!!')
