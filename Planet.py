# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:20:00 2018

@author: Student
"""

import pygame
from vec2d import Vec2d
from Matter import Matter

class Planet(Matter):
    def __init__(self, mass, vel, center, centerY, radius):
        self.mass = mass
        self.vel = Vec2d(0,0)
        self.centerX = center
        self.radius = radius
        
        