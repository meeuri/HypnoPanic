#pylint: disable=E1101
#pylint: disable=C0103
#pylint: disable=C0111
import pygame
#from vector import Vector
import settings
from vector import Vector
import threading

class Animal(pygame.sprite.Sprite):

    @property
    def tag(self):
        return self._tag

    def __init__(self, world):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.image = pygame.Surface((settings.ANIMAL_SIZE, settings.ANIMAL_SIZE))
        self.image.fill(settings.ANIMAL_COLOR)
        self.rect = self.image.get_rect()
        self.dir = Vector(0, 0)
        self.speed = settings.ANIMAL_SPEED
        self.has_control = True
        self.end_time = 0

    def  update(self):
        pass

    def get_rect(self):
        return self.rect

    def set_dir(self, dir):
        self.dir = dir.get_normalized()
        self.dir.x = round(self.dir.x, 1)
        self.dir.y = round(self.dir.y, 1)

    def move(self):
        delta_x = self.dir.x * self.speed
        delta_y = self.dir.y * self.speed
        self.rect.x += delta_x
        self.rect.y += delta_y
        self.check_disabled()

    def set_pos(self, pos):
        size_x, size_y = self.rect.size
        self.rect.x = pos.x - size_x/2
        self.rect.y = pos.y - size_y/2

    def set_group(self, group):
        self.add(group)

    def get_pos(self):
        size_x,  size_y = self.rect.size
        x = self.rect.x + size_x/2
        y = self.rect.y + size_y/2
        return Vector(x, y)

    def bordered(self, border):
        self.bounce(border)

    def bounce(self, border):
        if border in ('RIGHT', 'LEFT'):
            self.dir.x = -self.dir.x
        elif border in ('BOT', 'TOP'):
            self.dir.y = -self.dir.y

    def disable(self, frames):
        if self.has_control:
            self.has_control = False
            self.end_time = pygame.time.get_ticks() + frames
    
    def collide(self, actor):
        pass

    def die(self):
        self.world.report_death(self)

    def check_disabled(self):
        if not self.has_control:
            if self.end_time < pygame.time.get_ticks():
                self.has_control = True
        
