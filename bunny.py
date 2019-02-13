#pylint: disable=E1101
#pylint: disable=C0103
#pylint: disable=C0111
import pygame
#from vector import Vector
import settings
from vector import Vector
from animal import Animal

class Bunny(Animal):

    def __init__(self, world):
        super().__init__(world)
        self.image.fill(settings.BUNNY_COLOR)
        self.speed = settings.BUNNY_SPEED
        self._tag = 'BUNNY'

    def look(self):
        foxes = self.world.get_foxes()

        treats = list()
        for fox in foxes:
            dist = Vector.distance(self.get_pos(), fox.get_pos())
            if dist < settings.BUNNIES_RANGE:
                treats.append(fox)

        if treats:
            new_dir = Vector(0, 0)
            for treat in treats:
                new_dir += self.get_pos() - treat.get_pos()
                #self.world.draw_path(self.get_pos(), treat.get_pos(), settings.BUNNY_PATH_COLOR)
            self.set_dir(new_dir)

    def update(self):
        if self.has_control:
            self.look()
        self.move()

    def bordered(self, border):
        self.disable(settings.BUNNY_DISABLE_FRAMES)
        super().bordered(border)

    def collide(self, actor):
        if actor.tag == 'FOX':
            print('DIED')
            self.die()
