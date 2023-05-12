from AppSettings import AppSettings
from Vector2 import Vector2
from enum import IntEnum
from Board import Board
from PyGameContext import PyGameContext
from Entity import Entity

import pygame

class SnakeBody:
    Texture = None
    Position = Vector2(-1,-1)
    TileSize = (0,0)

    def __init__(self, new_pos, tile_size : tuple,texture = None):
        self.Position = new_pos
        self.TileSize = tile_size
        if texture is not None:
            self.Texture = texture

    def get_tile_size(self):
        return self.TileSize

    def get_position(self):
        return self.Position
    
    def get_texture(self):
        return self.Texture

class Snake(Entity):
    __VelocityVector = Vector2(1,1)
    __DirectionVector = Vector2(0,0)
    
    __TextureIndexToDraw = 0
    __Position = Vector2(-1,-1)
    __TileSize = (0,0)
    
    __BodyTexture = pygame.image.load("resources/snake/body.png")  

    __BodyMaxSize = 10

    __Texture = [pygame.image.load("resources/snake/head_left.png"),  
                 pygame.image.load("resources/snake/head_right.png"),
                 pygame.image.load("resources/snake/head_up.png"),
                 pygame.image.load("resources/snake/head_down.png")]
    
    __SnakeSegments = []

    def __init__(self, tile_size : tuple):
        self.__TileSize = tile_size
        self.__Position.x = AppSettings.instance.get_value("map_width") / 2
        self.__Position.y = AppSettings.instance.get_value("map_height") / 2

        self.__SnakeSegments = [SnakeBody(self.__Position,tile_size)]
        for tile in self.__Texture:
            tile = pygame.transform.smoothscale(tile,self.__TileSize)
       
    def __del__(self):
        pass
    
    def input_handler(self,dir_vector : Vector2):
        self.__DirectionVector = dir_vector     

    def update(self) -> None:
        if self.__DirectionVector.x == -1 and self.__DirectionVector.y == 0:
            self.__TextureIndexToDraw = 0
        
        if self.__DirectionVector.x == 1 and self.__DirectionVector.y == 0:
            self.__TextureIndexToDraw = 1
        
        if self.__DirectionVector.y == -1 and self.__DirectionVector.x == 0:
            self.__TextureIndexToDraw = 2
        if self.__DirectionVector.y == 1 and self.__DirectionVector.x == 0:
            self.__TextureIndexToDraw = 3

        #head position used as offset, to change position of snake body parts
        self.__SnakeSegments[0] = SnakeBody(self.__Position,self.__TileSize)

        #Update snake segments position
        for index in range(len(self.__SnakeSegments) - 1,0,-1):
            self.__SnakeSegments[index].Position = self.__SnakeSegments[index - 1].Position

        if not self.__DirectionVector.IsEmpty():
            self.__Position += (self.__VelocityVector * self.__DirectionVector)

        if self.__Position.x < 0 or self.__Position.x >= AppSettings.instance.get_value("map_width") or self.__Position.y < 0 or self.__Position.y >= AppSettings.instance.get_value("map_height"):
            self.__reset()

    def render(self):
        for body_part in self.__SnakeSegments:
            if body_part.Position != self.__Position:
                Board.render_entity(body_part)
    
    def on_resize(self,square_size : tuple) -> None:
        self.set_tile_size(square_size)
        for i in range(0,4):
            self.__Texture[i] = pygame.transform.smoothscale(self.__Texture[i],self.__TileSize)
        
        for body_part in self.__SnakeSegments:
            body_part.TileSize = square_size
    
    def set_tile_size(self, tile_size : tuple) -> None:
        self.__TileSize = tile_size

    def get_tile_size(self) -> tuple:
        return self.__TileSize
    
    def get_position(self) -> Vector2:
        return self.__Position

    def set_position(self,new_pos : Vector2) -> None:
        self.__Position = new_pos
    
    def get_texture(self) -> pygame.surface.Surface:
        return self.__Texture[self.__TextureIndexToDraw]

    def grow(self):
        if len(self.__SnakeSegments) < self.__BodyMaxSize:
            self.__SnakeSegments.append(SnakeBody(self.__Position,self.__TileSize,self.__BodyTexture))

    def __reset(self):
        self.__Position.x = AppSettings.instance.get_value("map_width") / 2
        self.__Position.y = AppSettings.instance.get_value("map_height") / 2
        self.__TextureIndexToDraw = 0
        self.__DirectionVector = Vector2(0,0)
        self.__SnakeSegments.clear()
        self.__SnakeSegments.append(SnakeBody(self.__Position,self.__TileSize))
