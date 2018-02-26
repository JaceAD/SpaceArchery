# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:28:08 2018

@author: Student
"""

import pygame
from LevelGenerator import LevelGenerator 
from vec2d import Vec2d
from coords import Coords
import ForceCalculator
from Matter import Arrow 
from Matter import Planet

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GRAY     = ( 127, 127, 127)

def main():
    pygame.init()
 
    width = 1200
    height = 900
    
    levelLoader = LevelGenerator()  #Loads planet layouts into planet array
    
    screen = pygame.display.set_mode([width,height])
    screen_center = Vec2d(width/2, height/2)
    coords = Coords(screen_center.copy(), 1, True)
    # ^ Center of window is (0,0), scale is 1:1, and +y is up
     
    coords.zoom_at_coords(Vec2d(0,0), 20)
    # ^Sets camera center
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    planets = [];
    planets = levelLoader.loadLevel(levelLoader.getLevel())
    arrow = Arrow(2, Vec2d(20, 500), Vec2d(0,0))
    
    frame_rate = 60
    playback_speed = 1
    done = False
    while not done:
        # --- Main event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # If user clicked close
                done = True
        
        if(arrow.getActive):
            #calculate all forces that would apply to arrow here
            print("Placeholder")
        else:
            #read user input here
            print("Placeholder")
        
        
            # Drawing
        screen.fill(BLACK) # wipe the screen
        for obj in planets:
            obj.draw(screen, coords) # draw object to screen
            obj.draw(draw_screen, coords) # add object to trail in draw_screen
        
        # --- Update the screen with what we've drawn.
        pygame.display.update()
    
        # This limits the loop to 60 frames per second
        clock.tick(frame_rate)
        
    pygame.quit()
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise e
