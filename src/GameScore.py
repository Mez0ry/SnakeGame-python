import pygame
import pygame.freetype
from PyGameContext import PyGameContext
from AppSettings import AppSettings


class GameScore:
    __Score = 0
    __Font = None
    __BackgroundTexture = None

    def __init__(self):
        self.__Score = 0
        self.__Font = pygame.freetype.Font("resources/fonts/HACKED.ttf", 20)
        self.__BackgroundTexture = pygame.image.load("resources/other/ScoreBar.png")

    def render(self):
        window_w, window_h = pygame.display.get_surface().get_size()
        text_surface,text_rect = self.__Font.render(str("Score: " + self.__Score.__str__()), (255,30,15),False,pygame.freetype.STYLE_OBLIQUE,0,20)
        offset = 10
        self.__BackgroundTexture = pygame.transform.smoothscale(self.__BackgroundTexture,(text_rect.width + offset,text_rect.height))
        
        PyGameContext.instance.get_window_surface().blit(self.__BackgroundTexture,(((window_w / 2) - text_rect.width / 2) - (offset / 2),text_rect.height))

        PyGameContext.instance.get_window_surface().blit(text_surface,((window_w / 2) - text_rect.width / 2,text_rect.height))
        
    ##operator overloading
    def __add__(self, other):
        self.__Score += other
    
    def __sub__(self, other):
        self.__Score -= other