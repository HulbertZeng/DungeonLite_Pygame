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
        self.fireLimit = 1
        self.spell = []

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

    def fireSpell(self, pygame, screen):
        if pygame.mouse.get_pressed()[0] and len(self.spell) != self.fireLimit:
            self.fired = True
            self.spell.append(projectile(self.x, self.y))
            for s in self.spell:
                if s.new:
                    s.fire()
                    s.new = False
        if self.fired:
            for s in self.spell:
                s.update(screen)
                if not(0 < s.x < 600 and 0 < s.y < 600):
                    self.spell.remove(s)
                if len(self.spell) == 0:
                    self.fired = False
                    break


class projectile:
    def __init__(self, x, y):
        self.img = pygame.image.load('images/energyBall.png')
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.vel = 25
        self.new = True

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
