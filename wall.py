import pygame
import random

class Wall():
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        if y == 0:
            self.rect = pygame.Rect(x, y, 40, random.randint(120, 240))
        else:
            height = random.randint(120, 240)
            self.rect = pygame.Rect(x, y - height, 40, height)

    def move(self):
        self.rect.x -= 2
    
    def isOut(self):
        if (self.rect.x + 40 <= 0):
            return True

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)

    def update(self):
        self.move()