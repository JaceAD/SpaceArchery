# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:36:09 2018

@author: Student
"""
from  Matter import Planet 
from vec2d import Vec2d

 
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
            self.planets.append(Planet(5, Vec2d(0,0), Vec2d(600,450), 15))
            self.planets.append(Planet(5, Vec2d(0,0), Vec2d(600,150), 15))
            self.planets.append(Planet(5, Vec2d(0,0), Vec2d(600,750), 15))
            return self.planets