import pygame
import math


class player:
    def __init__(self, x, y):
        self.left_img = pygame.image.load('images/wizardLeft.png')
        self.right_img = pygame.image.load('images/wizardRight.png')
        self.left = True
        self.right = False
        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.health = 120
        self.attack = 30
        self.vel = 9
        self.fired = False
        self.spell = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
        if keys[pygame.K_d] and self.x < 600 - self.width - self.vel:
            self.x += self.vel
            self.left = False
            self.right = True
        if keys[pygame.K_w] and self.y > self.vel:
            self.y -= self.vel
        if keys[pygame.K_s] and self.y < 600 - self.height - self.vel:
            self.y += self.vel


class projectile:
    def __init__(self, x, y):
        self.img = pygame.image.load('images/energyBall.png')
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.vel = 25

    #get dx and dy
    def fire(self):
        pmx, pmy = self.x, self.y
        mx, my = pygame.mouse.get_pos()

        radians = math.atan2(my - pmy, mx - pmx)
        self.dx = math.cos(radians) * self.vel
        self.dy = math.sin(radians) * self.vel

    #move by dx and dy
    def update(self, screen):
        self.x += self.dx
        self.y += self.dy
        screen.blit(self.img, (int(self.x), int(self.y)))
