#!/usr/bin/env python3

class Pet(object):
    num_pets = 0

    def __init__(self, name):
        self.name = name
        Pet.num_pets += 1
        self.num_pets = Pet.num_pets

    def speak(self):
        print("My name's %s and the number of pets is %d" % (self.name, Pet.num_pets))

rover = Pet("rover")
spot = Pet("spot")

rover.speak()
spot.speak()
