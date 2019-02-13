#pylint: disable=E1101
#pylint: disable=C0103
#pylint: disable=C0111
import pygame
#from vector import Vector
import settings
from vector import Vector
from fox import Fox
from bunny import Bunny

TOP = 1
RIGHT = 2
BOT = 3
LEFT = 4

class World():

    foxes = list()
    bunnies = list()

    def __init__(self, surface):
        self.actors = pygame.sprite.Group()
        self.surface = surface

        self.create_actor('FOX', Vector(100, 100))
        self.create_actor('BUNNY', Vector(150, 150))

        self.create_actor('BUNNY', Vector(40, 150))

        self.create_actor('BUNNY', Vector(70, 150))
        self.create_actor('BUNNY', Vector(80, 30))
        self.create_actor('BUNNY', Vector(90, 150))

        self.create_actor('BUNNY', Vector(10, 200))
        self.create_actor('BUNNY', Vector(10, 150))


    def update(self):
        self.detect_collides()
        for bunny in self.bunnies:
            bunny.update()
        for fox in self.foxes:
            fox.update()
        
        self.detect_borders()


    def draw(self):
        self.actors.draw(self.surface)

    def get_foxes(self):
        return self.foxes.copy()
    
    def get_bunnies(self):
        return self.bunnies.copy()

    def detect_collides(self):
        for active in self.actors.copy():
            for passive in self.actors.copy():
                if active.get_rect().colliderect(passive.get_rect()):
                    if active:
                        active.collide(passive)
          
    def detect_borders(self): 
        for actor in self.actors:
            rect = actor.get_rect()
            size_x, size_y = actor.get_rect().size
           
            if rect.x >= self.surface.get_width()  - size_x:
                actor.rect.x = self.surface.get_width() - size_x
                actor.bordered('RIGHT')
            
            if rect.x <= 0:
                actor.rect.x = 0
                actor.bordered('LEFT')
           
            if rect.y >= self.surface.get_height() - size_y:
                actor.rect.y = self.surface.get_height() - size_y
                actor.bordered('BOT')

            if rect.y <= 0:
                actor.rect.y = 0
                actor.bordered('TOP')

    @property
    def scene(self):
        return self.surface

    def report_death(self, actor):
        if actor.tag == 'BUNNY':
            self.infect(actor)
        
    def infect(self, bunny):
        pos = bunny.get_pos()
        self.create_actor('FOX', pos)
        bunny.kill()
        if bunny in self.bunnies: 
            self.bunnies.remove(bunny)

    def create_actor(self, tag, pos):
        if tag == 'BUNNY': 
            actor = Bunny(self)
            self.bunnies.append(actor) 
        elif tag == 'FOX':
            actor = Fox(self)
            self.foxes.append(actor)
        else:
            return
        actor.set_group(self.actors)
        actor.set_pos(pos)

    def draw_path(self, start, end, color):
        pygame.draw.line(self.scene, color, (start.x, start.y), (end.x, end.y))
