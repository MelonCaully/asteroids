# this allows us to use the code from the open-source pygame library
import pygame as pg
from constants import *

def main():
    pg.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill(000)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.display.flip()
    

if __name__ == "__main__":
    main()