#!/usr/bin/env python2

"""
    This is a python file to check if the containers
    with specific beer have exceeded the allowed
    refrigeration limit and alert the user

    input: array of containers
    output: containers where the temperature exceeded the refrigeration limit
"""
import config

__all__ = []
__version__ = '0.1'
__author__ = 'Mani shanker Talusani'

try:
    from random import randint
except ImportError:
    raise ImportError('random module is not installed, refer README')

# I am assuming the truck can hold 100 containers
TOTAL_CONTAINERS = 100


class Beer(object):
    """
        Class definition of the Beer.

        attribues: beer name, temperature range

    """
    beer_names = config.beer_names
    beer_temp = config.beer_temp

    def __init__(self, name=None, temp_range=(0, 0)):
        self.name = name
        self.low_temp = temp_range[0]
        self.high_temp = temp_range[1]

    def __str__(self):
        return self.name


class Container(Beer):
    """

        Class definition of the Container

        attributes: beer name, temperature range, set temperature, thermometer temperature, quantity
    """

    def __init__(self, name, temp_range, set_temp=0, quantity=0, number=0):
        Beer.__init__(self, name, temp_range)
        self.set_temp = set_temp
        self.thermometer_temp = 0
        self.quantity = quantity
        self.number = number

    def get_temp(self):
        self.thermometer_temp = randint(config.temp_range[0], config.temp_range[1])
        return self.thermometer_temp

    def alert(self):
        if self.low_temp <= self.get_temp() <= self.high_temp:
            print(self.thermometer_temp)
            return self.thermometer_temp
        else:
            print("Hey Baz, container with %s is out of refrigeration range" % self.number)


if __name__ == '__main__':
    # b = Beer(Beer.beer_names[0], Beer.beer_temp[0])
    c = Container("beer 1", (4, 6), 5, 10, 55)
    is_driving = True
    for x in range(1, 10):
        c.alert()
