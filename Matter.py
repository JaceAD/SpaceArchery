# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:04:47 2018

@author: Student
"""
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GRAY     = ( 127, 127, 127)
BROWN    = ( 165,  42,  42)

import pygame
from vec2d import Vec2d

class Matter:
    def __init__(self, mass, center, vel):
        self.vel = vel
        self.mass = mass
        self.center = center
        self.mom = self.vel*self.mass
        self.force = Vec2d(0,0)
        self.color = GRAY
    
    def update_mom(self, dt):
        self.mom += self.force*dt
    def update_vel(self):
        self.vel.copy_in(self.mom/self.mass)
    def update_pos(self, dt):
        self.center += self.vel*dt
        
        
class Planet(Matter):
    def __init__(self, mass, vel, center, radius):
        Matter.__init__(self, mass, center, vel)
        self.radius = radius
        self.color = RED
        
    def setColor(self, color):
        self.color = color
    
    def draw(self, screen, coords):
        pygame.draw.circle(screen, self.color, 
                           coords.pos_to_screen(self.center).int(), 
                           int(coords.scalar_to_screen(self.radius)), 0)
        
        
class Arrow(Matter):
    #Init that calls parent.
    #Sets position vec2d of tip, which can be used with center to determine facing of arrow
    #Sets active to false. While false, gravitational forces will not act upon it (if statement in main loop performs this check)
    def __init__(self, mass, center, vel, tip):
        Matter.__init__(self, mass, center, vel)
        self.tip = tip
        self.force = Vec2d(0,0)
        self.active = False
        self.color = BROWN
        self.tipColor = GRAY
        self.base = self.center - self.tip
        
    def getActive(self):
        return self.active
    
    def setActive(self, state):
        self.active = state
        
    def update_pos(self, dt):
        self.center += self.vel*dt
        self.tip += self.vel*dt
        self.base += self.vel*dt
    
    def draw(self, screen, coords):
        #Bottom of arrow. Assumes tip is the tip of shaft and arrowhead has no mass
        base = self.center - self.tip
        
        #Vectors representing the arrow's direction
        arrowVec = base + self.tip
        normalizedArrowVec = arrowVec.normalized() 
        perpendicularArrowVec = normalizedArrowVec.perpendicular()
        
        #A set of vec2d points for the arrowhead
        tipForward = self.tip + normalizedArrowVec*4
        tipSide1 = self.tip + perpendicularArrowVec*2
        tipSide2 = self.tip - perpendicularArrowVec*2
        tipList = [coords.pos_to_screen(tipForward).int(),coords.pos_to_screen(tipSide1).int(),coords.pos_to_screen(tipSide2).int()]
        
        #Draws line and triangular arrowhead
        pygame.draw.line(screen, self.color, coords.pos_to_screen(base).int(), coords.pos_to_screen(self.tip).int(), width=8)
        pygame.draw.polygon(screen, self.color, tipList, width=0)