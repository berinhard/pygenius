# -*- encoding:utf-8 -*-
import pygame
import time
import random

global screen, genius_rect, images

size = (660, 660)

pygame.init()
screen = pygame.display.set_mode(size)

screen.fill((0, 0, 0))

images = {
    'genius':pygame.image.load('images/genius.png').convert_alpha(),
    'blink_red':pygame.image.load('images/blink_red.png').convert_alpha(),
    'blink_yellow':pygame.image.load('images/blink_yellow.png').convert_alpha(),
    'blink_green':pygame.image.load('images/blink_green.png').convert_alpha(),
    'blink_blue':pygame.image.load('images/blink_blue.png').convert_alpha(),
}
genius_rect = images['genius'].get_rect()

def blink_list(sequence_list):
    for color in sequence_list:
        screen.blit(images[color], genius_rect)
        pygame.display.flip()
        time.sleep(1)
        screen.blit(images['genius'], genius_rect)
        pygame.display.flip()
        time.sleep(1)

def get_random_color():
    color_list = images.keys()
    color_list.remove('genius')
    return random.choice(color_list)

color_list = []

while True:
    color_list.append(get_random_color())
    blink_list(color_list)
