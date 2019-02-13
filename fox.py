#pylint: disable=E1101
#pylint: disable=C0103
#pylint: disable=C0111
import pygame
#from vector import Vector
import settings
from vector import Vector
from animal import Animal
from random import random

class Fox(Animal):
    def __init__(self, world):
        super().__init__(world)
        self.image.fill(settings.FOX_COLOR)
        self.speed = settings.FOX_SPEED
        self._tag = 'FOX'
        self.set_dir(Vector(random(), random()))
        self.disable(settings.FOX_DISABLE_FRAMES)

    def update(self):
        if self.has_control:
            self.look()
        self.move()

    def look(self):
        bunnies = self.world.get_bunnies()

        min_dist = self.world.scene.get_height() * self.world.scene.get_height()
        closest = None
        for bunny in bunnies:
            dist = Vector.distance(self.get_pos(), bunny.get_pos())
            if dist < min_dist:
                min_dist = dist
                closest = bunny

        if closest:
            new_dir = closest.get_pos() - self.get_pos()
            self.set_dir(new_dir)
            self.world.draw_path(self.get_pos(), closest.get_pos(), settings.FOX_PATH_COLOR)

    def bordered(self, border):
        self.bounce(border)