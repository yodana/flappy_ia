import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 60)
        self.x = x
        self.y = y
        self.isJump = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)

    def fall(self):
        self.rect.y += 2

    def jump(self):
        self.rect.y -= 20
        self.isJump += 20

    def collision(self, wall):
        print(self.rect)
        return self.rect.colliderect(wall)

    def update(self):
        if self.isJump > 0 and self.isJump <= 100:
            self.jump()
        else:
            self.isJump = 0
            self.fall()