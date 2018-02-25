# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:14:58 2018

@author: Student
"""

import pygame
from vec2d import Vec2d
from Matter import Matter

class Arrow(Matter):
    def __init__(self, mass, vel):
        self.vel = vel
        self.mass = mass
        self.force = Vec2d(0,0)
        self.active = False
        
    def getActive(self):
        return self.active