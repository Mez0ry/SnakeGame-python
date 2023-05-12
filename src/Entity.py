from abc import ABC, abstractmethod
from Vector2 import Vector2
import pygame

class Entity(ABC):


    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def on_resize(self,square_size : tuple) -> None:
        pass

    @abstractmethod
    def set_tile_size(self, tile_size : tuple) -> None:
         pass

    @abstractmethod
    def get_tile_size(self) -> tuple:
        pass
    
    @abstractmethod
    def get_position(self) -> Vector2:
        pass
    
    @abstractmethod
    def set_position(self,new_pos : Vector2) -> None:
        pass
    
    @abstractmethod
    def get_texture(self) -> pygame.surface.Surface:
        pass