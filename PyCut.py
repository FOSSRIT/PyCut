#!/usr/bin/python
import pygame
from game import PyCutGame as PyCut

def main():
    pygame.init()
    pygame.display.set_mode((1200, 900), pygame.RESIZABLE)
    game_instance = PyCut()
    game_instance.run()

if __name__ == '__main__':
    main()
