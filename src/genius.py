# -*- encoding:utf-8 -*-
import pygame

size = (660, 660)

pygame.init()
screen = pygame.display.set_mode(size)

images = {
    'genius':pygame.image.load('images/genius.png').convert_alpha(),
    'blink_red':pygame.image.load('images/blink_red.png').convert_alpha(),
    'blink_yellow':pygame.image.load('images/blink_yellow.png').convert_alpha(),
    'blink_green':pygame.image.load('images/blink_green.png').convert_alpha(),
    'blink_blue':pygame.image.load('images/blink_blue.png').convert_alpha(),
}
genius_rect = images['genius'].get_rect()

screen.fill((0, 0, 0))

while True:
    screen.blit(images['genius'], genius_rect)
    pygame.display.flip()
    screen.blit(images['blink_red'], genius_rect)
    pygame.display.flip()
    screen.blit(images['blink_yellow'], genius_rect)
    pygame.display.flip()
    screen.blit(images['blink_green'], genius_rect)
    pygame.display.flip()
    screen.blit(images['blink_blue'], genius_rect)
    pygame.display.flip()
