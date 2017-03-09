import unittest
from pet_factory import Dog, Cat, spawn_pet

class TestPetBehavior(unittest.TestCase):

    def test_dog_properties(self):
        D = Dog('Hound')
        # self.assertRaises(AttributeError, lambda: D._name)
        self.assertEqual(D._name, 'Hound')
