#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A dwelling builder
"""


class Director(object):

    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


class Builder(object):
    """
    Abstract Builder
    """

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError


class BuilderHouse(Builder):
    """Concrete Builder"""

    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):

    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


class Building(object):
    """Product"""

    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)

director = Director()
director.builder = BuilderHouse()
director.construct_building()
building = director.get_building()
print(building)
director.builder = BuilderFlat()
director.construct_building()
building = director.get_building()
print(building)
