import pygame
import math


class enemy:
    def __init__(self, x, y, vel):
        self.attack_img = pygame.image.load('images/attack.png')
        self.explode_img = pygame.image.load('images/explode.png')
        self.left_img = pygame.image.load('images/demonLeft.png')
        self.right_img = pygame.image.load('images/demonRight.png')
        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.health = 90
        self.attack = 10
        self.vel = vel
        self.dx = 0
        self.dy = 0
        self.pmx = x
        self.pmy = y
        self.dist = 0

    #get dx and dy
    def follow(self, mx, my):
        radians = math.atan2(my - self.pmy, mx - self.pmx)
        self.dist = math.hypot(mx - self.pmx, my - self.pmy) / self.vel
        self.dist = int(self.dist)

        self.dx = math.cos(radians) * self.vel
        self.dy = math.sin(radians) * self.vel

        self.pmx, self.pmy = mx, my

    #move by dx and dy
    def update(self, screen):
        if self.dist > 0:
            self.dist -= 1
            self.x += self.dx
            self.y += self.dy
        demon_img = 0
        if self.dx < 0:
            demon_img = self.left_img
        else:
            demon_img = self.right_img
        screen.blit(demon_img, (int(self.x), int(self.y)))
