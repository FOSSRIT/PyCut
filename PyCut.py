#!/usr/bin/python
import game

class PyCut():
    def __init__(self):
        self.game_instance = game.PyCutGame()

    # Calls The main game loop.
    def run(self):
        self.game_instance.run()

def main():
    PyCut().run()

if __name__ == '__main__':
    main()
