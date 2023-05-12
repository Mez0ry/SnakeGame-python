import pygame
import random

class PyGameContext:
    __m_WindowSurface = None

    def __new__(cls,data_json):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PyGameContext,cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        pass
    
    def __init__(self, obj_AppSettings):
        #initializing pygame
        pygame.init()
        if pygame.get_init():
            print("Pygame: successfully initialized\n")
        
        #initializing display
        pygame.display.init()
        if pygame.display.get_init():
            print("Pygame display: successfuly initialized")
        
        # freetype
        pygame.freetype.init()
        if pygame.freetype.get_init():
            print("pygame.freetype: successfully initialized")
        
        window_flags = pygame.RESIZABLE

        if obj_AppSettings.get_value("fullscreen_mode"):
            window_flags += pygame.FULLSCREEN
        
        #creating window and setuping header name of window
        self.__m_WindowSurface = pygame.display.set_mode([obj_AppSettings.get_value("window_width"),obj_AppSettings.get_value("window_height")],window_flags)
        pygame.display.set_caption("SnakeGame-python")

    def __enter__(self):
        return self

    def __cleanup(self):
        pygame.display.quit()
        pygame.freetype.quit()
        pygame.quit()
    
    def __del__(self):
       self.__cleanup()
    
    def get_window_surface(self):
        return self.__m_WindowSurface