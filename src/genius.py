# -*- encoding:utf-8 -*-
import pygame
import time
import random
import sys

from genius_classes import *

global screen, genius_rect, images, player_time

size = (660, 660)

pygame.init()
screen = pygame.display.set_mode(size)

screen.fill((0, 0, 0))

images = {
    'genius':pygame.image.load('images/genius.png').convert_alpha(),
    RED:pygame.image.load('images/blink_red.png').convert_alpha(),
    YELLOW:pygame.image.load('images/blink_yellow.png').convert_alpha(),
    GREEN:pygame.image.load('images/blink_green.png').convert_alpha(),
    BLUE:pygame.image.load('images/blink_blue.png').convert_alpha(),
}
genius_rect = GeniusRect(images['genius'].get_rect())

def blink_list(sequence_list):
    time.sleep(1)
    for color in sequence_list:
        blink_color(color)
        time.sleep(0.5)

def blink_color(color):
    screen.blit(images[color], genius_rect.rect)
    pygame.display.flip()
    time.sleep(0.5)
    screen.blit(images['genius'], genius_rect.rect)
    pygame.display.flip()

def get_random_color():
    color_list = images.keys()
    color_list.remove('genius')
    return random.choice(color_list)

def mouse_click(event):
    left = 1
    return event.type == pygame.MOUSEBUTTONDOWN and event.button == left

def main_loop():
    color_list = []
    player_time = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif player_time and mouse_click(event):
                print genius_rect.get_area_clicked(event.pos)
                player_time = False
        if not player_time:
            color_list.append(get_random_color())
            blink_list(color_list)
            player_time = True

if __name__ == '__main__':
    main_loop()
