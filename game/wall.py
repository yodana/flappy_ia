import pygame
import random

class Wall():
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.height = random.randint(120, 240)
        if y == 0:
            img = pygame.image.load("assets/pipe-green.png").convert()
            self.image = pygame.transform.rotate(img, 180)
            self.rect = pygame.Rect(x, y, 40, self.height)
        else:
            self.image = pygame.image.load("assets/pipe-green.png").convert()
            self.rect = pygame.Rect(x, y - self.height, 40, self.height)

    def move(self):
        self.rect.x -= 2
    
    def isOut(self):
        if (self.rect.x + 40 <= 0):
            return True

    def draw(self, screen):
        #pygame.draw.rect(screen, (255,0,0), self.rect)
        if self.y == 0:
            screen.blit(self.image, (self.rect.x, self.rect.y - (self.image.get_height() - self.height)))
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.move()