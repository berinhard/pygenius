# -*- encoding:utf-8 -*-
from pygame import Rect

class GeniusRect():

    def __init__(self, rect):
        self.rect = rect
        self.area_1 = self.__set_area_1()
        self.area_2 = self.__set_area_2()
        self.area_3 = self.__set_area_3()
        self.area_4 = self.__set_area_4()

    def __set_area_1(self):
        top = self.rect.top
        left = self.rect.left
        height = int(self.rect.height / 2)
        width = int(self.rect.width / 2)
        return Rect(left, top, width, height)

    def __set_area_2(self):
        top = self.rect.top
        left = int(self.rect.width / 2)
        height = int(self.rect.height / 2)
        width = int(self.rect.width / 2)
        return Rect(left, top, width, height)

    def __set_area_3(self):
        top = int(self.rect.height / 2)
        left = self.rect.left
        height = int(self.rect.height / 2)
        width = int(self.rect.width / 2)
        return Rect(left, top, width, height)

    def __set_area_4(self):
        top = int(self.rect.height / 2)
        left = int(self.rect.width / 2)
        height = int(self.rect.height / 2)
        width = int(self.rect.width / 2)
        return Rect(left, top, width, height)
