# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:36:09 2018

@author: Student
"""
from  Matter import Planet 
from vec2d import Vec2d

 # Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GRAY     = ( 127, 127, 127)
BROWN    = ( 165,  42,  42)

class LevelGenerator:
    def __init__(self):
        self.levelNum = 1
        self.planets = []
    
    def getLevel(self):
        return self.levelNum
    def setLevel(self, targetLevel):
        self.levelNum = targetLevel
        
    def loadLevel(self, level):
        self.planets = []
        if(level == 1):
            self.planets.append(Planet(5000, Vec2d(0,0), Vec2d(-200,0), 25))
            self.planets.append(Planet(5000, Vec2d(0,0), Vec2d(-200,-300), 25))
            self.planets.append(Planet(5000, Vec2d(0,0), Vec2d(-200,300), 25))
            self.planets.append(Planet(12000, Vec2d(0,0), Vec2d(200, 0), 35))
            self.planets[3].setColor(BLUE)
            return self.planets