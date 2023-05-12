from Vector2 import Vector2
from AppSettings import AppSettings
from PyGameContext import PyGameContext
from enum import IntEnum
import pygame
import random
from GameScore import GameScore
from Entity import Entity

class FoodType(IntEnum):
    APPLE =0,
    BURGER = 1,
    HOTDOG = 2,
    MANGO = 3,
    STAR_FRUIT = 4,
    STEAK = 5,
    WATER_MELON = 6


class Food(Entity):
    __Texture = None
    __TileSize = (0,0)
    __Position = Vector2(-1,-1)
    __Points = 0

    def __init__(self,tile_size : tuple):
        self.__TileSize = tile_size
        self.__respawn_random_food()
        self.__Position = self.__get_random_pos()

    def update(self) -> None:
        pass

    def get_points(self):
        return self.__Points
    
    def get_position(self) -> Vector2:
        return self.__Position

    def set_position(self,new_pos : Vector2) -> None:
        self.__Position = new_pos
    
    def get_texture(self) -> pygame.surface.Surface:
        return self.__Texture
    
    def on_resize(self,square_size : tuple) -> None:
        self.set_tile_size(square_size)
        self.__Texture = pygame.transform.smoothscale(self.__Texture,self.__TileSize)

    def set_tile_size(self, tile_size : tuple) -> None:
        self.__TileSize = tile_size

    def get_tile_size(self) -> tuple:
        return self.__TileSize

    def respawn_curr_food(self) -> None:
        self.__respawn_random_food()
        self.__Position = self.__get_random_pos()

    def __respawn_random_food(self):
        rand_int = random.randint(0,6)
        match FoodType(rand_int):
            case FoodType.APPLE:
                self.__Texture = pygame.image.load("resources/food/apple.png")
                self.__Points = 2

            case FoodType.BURGER:
                self.__Texture = pygame.image.load("resources/food/burger.png")
                self.__Points = -6

            case FoodType.HOTDOG:
                self.__Texture = pygame.image.load("resources/food/hotdog.png")
                self.__Points = -4
            case FoodType.MANGO:
                self.__Texture = pygame.image.load("resources/food/mango.png")
                self.__Points = 4

            case FoodType.STAR_FRUIT:
                self.__Texture = pygame.image.load("resources/food/star_fruit.png")
                self.__Points = 10
            case FoodType.STEAK:
                self.__Texture = pygame.image.load("resources/food/steak.png")
                self.__Points = -5
            case FoodType.WATER_MELON:
                self.__Points = 8
                self.__Texture = pygame.image.load("resources/food/water_melon.png")
        
        self.__Texture = pygame.transform.smoothscale(self.__Texture,self.__TileSize)
    
    def __get_random_pos(self) -> Vector2:
       pos_x = random.randint(0,AppSettings.instance.get_value("map_width") - 1)
       pos_y = random.randint(0,AppSettings.instance.get_value("map_height") - 1)
       return Vector2(pos_x,pos_y)