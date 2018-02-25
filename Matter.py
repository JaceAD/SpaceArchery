# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:04:47 2018

@author: Student
"""

import pygame
from vec2d import Vec2d

class Matter:
    def __init__(self, mass, center, vel):
        self.vel = vel
        self.mass = mass
        self.center = center
        self.mom = self.vel*self.mass
        self.force = Vec2d(0,0)
    
    def update_mom(self, dt):
        self.mom += self.force*dt
    def update_vel(self):
        self.vel.copy_in(self.mom/self.mass)
    def update_pos(self, dt):
        self.pos += self.vel*dt

    #need an update force function here too to update the force on the object
    #draw the objects and have the arrow and planet files have the draw function as well          
    def draw(self, screen, coords):
        pygame.draw.circle(screen, self.color, 
                           coords.pos_to_screen(self.pos).int(), 
                           int(coords.scalar_to_screen(self.radius)), 0)
        
        
class Planet(Matter):
    def __init__(self, mass, vel, center, radius):
        Matter.__init__(self, mass, center, vel)
        self.radius = radius
        
        
class Arrow(Matter):
    def __init__(self, mass, center, vel):
        Matter.__init__(self, mass, center, vel) 
        self.force = Vec2d(0,0)
        self.active = False
        
    def getActive(self):
        return self.active