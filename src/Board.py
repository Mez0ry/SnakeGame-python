from Vector2 import Vector2
from AppSettings import AppSettings
from PyGameContext import PyGameContext
from typing import Tuple, TypeVar
from Food import Food

from Entity import Entity

import pygame

class Board:
    __BoardTopLeft = Vector2(0,0)
    __TileSize = tuple()
    __Board = None
    __Texture = pygame.image.load("resources/map/map_texture.png")
    __MapSize = None
    
    def __init__(self, tile_size : Tuple):
        self.__TileSize = tile_size
        self.__MapSize = Vector2(AppSettings.instance.get_value("map_width"),AppSettings.instance.get_value("map_height"))
        self.__Board = [[0 for j in range(self.__MapSize.x)] for i in range(self.__MapSize.y)]
        self.__Texture = pygame.transform.scale(self.__Texture,self.__TileSize)
        self.on_resize()
    
    def render(self):
        tile_w ,tile_h  = self.__TileSize

        for y in range(0,self.__MapSize.y):
            for x in range(0,self.__MapSize.x):
                PyGameContext.instance.get_window_surface().blit(self.__Texture, [self.__BoardTopLeft.x + x * tile_w,self.__BoardTopLeft.y + y * tile_h])
    
    
    def on_resize(self):
        window_w, window_h = pygame.display.get_surface().get_size()
        tile_w,tile_h = self.__TileSize
        
        self.__BoardTopLeft.x = (window_w - (tile_w * AppSettings.instance.get_value("map_width"))) * 0.5
        self.__BoardTopLeft.y = (window_h - (tile_h * AppSettings.instance.get_value("map_height"))) * 0.5

        square_width  = (window_w * 0.8 / (AppSettings.instance.get_value("map_width") * 0.8))
        square_height  = (window_h * 0.8 / (AppSettings.instance.get_value("map_height") * 0.8))

        if square_width > square_height:
            square_width = square_height
        else:
            square_height = square_width

        self.__TileSize = (square_width,square_height)
        
        self.__Texture = pygame.transform.smoothscale(self.__Texture,self.__TileSize)
    
    def get_tile_size(self) -> tuple:
        return self.__TileSize
    
    @staticmethod
    def is_on_board(entity : Entity) -> bool:
        """Used to check whether entity on the board or no

        Parameters
        ----------
        entity : all derived classes from Entity
        """
        pos : Vector2 = entity.get_position()
        return not (pos.x >= AppSettings.instance.get_value("map_width") or pos.x < 0 or pos.y >= AppSettings.instance.get_value("map_height")  or pos.y < 0 )
    
    @staticmethod
    def render_entity(entity : Entity) -> None:
        if entity.get_texture() == None:
            return None
        
        """Used to render entity on the map

        Parameters
        ----------
        entity : all derived classes from Entity
        """
        if not Board.is_on_board(entity):
            return None
        
        tile_w, tile_h = entity.get_tile_size()
        
        PyGameContext.instance.get_window_surface().blit(entity.get_texture(),[Board.__BoardTopLeft.x + entity.get_position().x * tile_w,Board.__BoardTopLeft.y + entity.get_position().y * tile_h])