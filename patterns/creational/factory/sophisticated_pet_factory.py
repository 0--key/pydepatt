#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A pet factory abstraction
"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):

    def do_say(self):
        return "Bhow Bhow!!"


class Cat(Animal):

    def do_say(self):
        return "Meow Meow!!"


class PetFactory(object):

    def make_clamor(self, object_type):
        return eval(object_type)().do_say()
