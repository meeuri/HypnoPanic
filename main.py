#pylint: disable=E1101
#pylint: disable=C0103
import pygame
import animal
from vector import Vector
from bunny import Bunny
from world import World
import settings

pygame.init()
screen = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()
running = True
my_world = World(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(settings.GAME_SCREEN_COLOR)
    my_world.update()
    my_world.draw()
    pygame.display.update()
    clock.tick(settings.GAME_FRAME_RATE)
