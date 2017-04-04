#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discover how it works
"""
import unittest
from sophisticated_pet_factory import Dog, \
    Cat, PetFactory


class TestPetBehavior(unittest.TestCase):

    def setUp(self):
        self.pet_factory = PetFactory()


    def test_dog_speak_ability(self):
        self.assertEqual(
            self.pet_factory.make_clamor('Dog'),
            'Bhow Bhow!!')

    def test_cat_speak_ability(self):
        self.assertEqual(
            self.pet_factory.make_clamor('Cat'),
            'Meow Meow!!')

    def tearDown(self):
        del self.pet_factory
