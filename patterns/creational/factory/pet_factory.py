#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A pet factory abstraction
"""


class Dog(object):
    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat(object):
    """A simple cat class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def spawn_pet(pet="dog"):
    """The factory method"""
    pets = dict(dog=Dog("Hope"),
                cat=Cat("Peace"))
    return pets[pet]

d = spawn_pet("dog")
print(d.speak())
c = spawn_pet("cat")
print(c.speak())
