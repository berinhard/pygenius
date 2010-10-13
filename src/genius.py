# -*- encoding:utf-8 -*-
import pygame
import time
import random
import sys

from genius_classes import *

BLACK = (0, 0, 0)

class GeniusGame(object):

    def __init__(self, size):
        pygame.init()

        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(BLACK)

        self.images = {
            'genius':pygame.image.load('images/genius.png').convert_alpha(),
            RED:pygame.image.load('images/blink_red.png').convert_alpha(),
            YELLOW:pygame.image.load('images/blink_yellow.png').convert_alpha(),
            GREEN:pygame.image.load('images/blink_green.png').convert_alpha(),
            BLUE:pygame.image.load('images/blink_blue.png').convert_alpha(),
        }
        self.genius_rect = GeniusRect(self.images['genius'].get_rect())

        self.color_list = []
        self.player_answers = []

    def blink_genius_list(self):
        time.sleep(1)
        for color in self.color_list:
            self.blink_color(color)
            time.sleep(0.5)

    def blink_color(self, color):
        self.screen.blit(self.images[color], self.genius_rect.rect)
        pygame.display.flip()
        time.sleep(0.5)
        self.screen.blit(self.images['genius'], self.genius_rect.rect)
        pygame.display.flip()

    def get_random_color(self):
        color_list = self.images.keys()
        color_list.remove('genius')
        return random.choice(color_list)

    def mouse_click(self, event):
        left = 1
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == left

    def handle_player_answer(self, area):
        next_color_pos = len(self.player_answers)
        if self.color_list[next_color_pos] == area:
            self.player_answers.append(area)
            self.blink_color(area)
        else:
            print 'perdeu babaca!!!!'
            sys.exit(0)

    def continue_playing(self):
        return len(self.player_answers) != len(self.color_list)

    def main_loop(self):
        player_time = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif player_time and self.mouse_click(event):
                    area = self.genius_rect.get_area_clicked(event.pos)
                    if area:
                        self.handle_player_answer(area)
                        player_time = self.continue_playing()
            if not player_time:
                self.color_list.append(self.get_random_color())
                self.blink_genius_list()
                player_time = True
                self.player_answers = []

if __name__ == '__main__':
    game = GeniusGame((660, 660))
    game.main_loop()
