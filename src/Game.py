from AppSettings import AppSettings
from PyGameContext import PyGameContext
from Board import Board
from Snake import Snake
from Vector2 import Vector2
from Food import Food
from GameScore import GameScore
import asyncio

import pygame

class Game:
    __IsRunning = False
    __Clock = None
    __Board = None
    __Snake = None
    __FoodList = list()
    __GameScore = None

    def __init__(self):
        obj_AppSettings = AppSettings("config")
        obj_PyGameContext = PyGameContext(obj_AppSettings)
        
        self.Board = Board((20,20))
        self.__IsRunning = True
        self.__Clock = pygame.time.Clock()
        self.__Snake = Snake((20,20))
        self.__FoodList = [Food((40,20)),Food((40,40)),Food((40,40)),Food((40,40)),Food((40,40)),Food((40,40))]

        self.__GameScore = GameScore()

        self.Board.on_resize()
        self.__Snake.on_resize(self.Board.get_tile_size())

        for i in range(0,self.__FoodList.__len__()):
            self.__FoodList[i].on_resize(self.Board.get_tile_size())
        
    def __enter__(self):
        return self
    
    def __exit__(self,exc_type, exc_value, traceback):
        pass
    
    def play(self) -> None:
        PyGameContext.instance.get_window_surface().fill((140,40,145))

        arbitary_tuning : float = 5000 / AppSettings.instance.get_value("fps")

        old_time : float = pygame.time.get_ticks()

        while(self.__IsRunning):
            new_time : float  = pygame.time.get_ticks()
            
            PyGameContext.instance.get_window_surface().fill((140,40,145))

            self.__Clock.tick(AppSettings.instance.get_value("fps"))

            self.__input_handler()

            self.__update()

            self.__render()

            pygame.display.update()
            pygame.display.flip()

            frame_time : float = new_time - old_time
            old_time = new_time
            if arbitary_tuning > frame_time:
                pygame.time.delay(int(arbitary_tuning - frame_time))

    def __input_handler(self) -> None:
        direction = Vector2(0,0)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.__IsRunning = False
                case pygame.VIDEORESIZE:
                    self.Board.on_resize()
                    self.__Snake.on_resize(self.Board.get_tile_size())

                    for i in range(0,self.__FoodList.__len__()):
                        self.__FoodList[i].on_resize(self.Board.get_tile_size())
                 

                case pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        direction = Vector2(-1,0)
                    if event.key == pygame.K_RIGHT:
                        direction = Vector2(1,0)
                    if event.key == pygame.K_UP:
                        direction = Vector2(0,-1)
                    if event.key == pygame.K_DOWN:
                        direction = Vector2(0,1)
                    
                    self.__Snake.input_handler(direction)


    
    def __update(self) -> None:
        self.__Snake.update()

        for food in self.__FoodList:
            if food.get_position() == self.__Snake.get_position():
                self.__GameScore + food.get_points()
                self.__Snake.grow()
                food.respawn_curr_food()

    def __render(self) -> None:
        self.Board.render()
        Board.render_entity(self.__Snake)

        for food in self.__FoodList:
            Board.render_entity(food)
        
        self.__Snake.render()
        self.__GameScore.render()