# -*- encoding:utf-8 -*-
import pygame
import time
import random
import sys

from genius_classes import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def mouse_click(event):
    left = 1
    return event.type == pygame.MOUSEBUTTONDOWN and event.button == left

def key_pressed(event, key):
    return event.type == pygame.KEYDOWN and event.key == key


class GeniusGame(object):

    def __init__(self, size):
        pygame.init()

        self.size = size
        self.screen = pygame.display.set_mode(size)

        self.images = {
            'genius':pygame.image.load('images/genius.png').convert_alpha(),
            RED:pygame.image.load('images/blink_red.png').convert_alpha(),
            YELLOW:pygame.image.load('images/blink_yellow.png').convert_alpha(),
            GREEN:pygame.image.load('images/blink_green.png').convert_alpha(),
            BLUE:pygame.image.load('images/blink_blue.png').convert_alpha(),
        }
        image_rect = self.images['genius'].get_rect()
        image_rect.move_ip(35, 0)
        self.screen.fill(BLACK)
        self.genius_rect = GeniusRect(image_rect)
        self.screen.blit(self.images['genius'], self.genius_rect.rect)

        self.font = pygame.font.Font(None, 30)
        text = self.font.render(u'Aperte <SPACE> para Começar!', 0, WHITE)
        self.text_rect = text.get_rect()
        self.text_rect.move_ip(200, 630)
        self.screen.blit(text, self.text_rect)

        pygame.display.flip()

        self.color_list = []
        self.player_answers = []
        self.player_time = False
        self.game_started = False

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

    def handle_player_answer(self, area):
        next_color_pos = len(self.player_answers)
        if self.color_list[next_color_pos] == area:
            self.player_answers.append(area)
            self.blink_color(area)
        else:
            text = self.font.render(u'Você perdeu! Pontuação: %s... Aperte <SPACE> para jogar de novo!' % str(len(self.color_list) - 1), 0, WHITE)
            self.text_rect.move_ip(-190, 0)
            self.screen.blit(text, self.text_rect)
            self.game_started = False
            pygame.display.flip()

    def continue_playing(self):
        return len(self.player_answers) != len(self.color_list)

    def is_player_time(self):
        return self.player_time and self.game_started

    def is_genius_time(self):
        return not self.player_time and self.game_started

    def start_game_enviroment(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.images['genius'], self.genius_rect.rect)
        pygame.display.flip()

        self.game_started = True
        self.color_list = []
        self.player_answers = []
        self.player_time = False

    def main_loop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.is_player_time() and mouse_click(event):
                    area = self.genius_rect.get_area_clicked(event.pos)
                    if area and self.screen.get_at(event.pos) != BLACK:
                        self.handle_player_answer(area)
                        self.player_time = self.continue_playing()
                elif not self.game_started and key_pressed(event, pygame.K_SPACE):
                    self.start_game_enviroment()

            if self.is_genius_time():
                self.color_list.append(self.get_random_color())
                self.blink_genius_list()
                self.player_time = True
                self.player_answers = []

if __name__ == '__main__':
    game = GeniusGame((660, 660))
    game.main_loop()
