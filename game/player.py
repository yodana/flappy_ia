import pygame
import neat
class Player:
    def __init__(self, x, y, genome=None, net=None):
        self.rect = pygame.Rect(x, y, 70, 50)
        self.x = x
        self.y = y
        self.isJump = 0
        self.image = self.create_img("assets/redbird.png")
        self.score = 0
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render(f'{self.score}', True, (0, 0, 0))
        self.alive = 1
        self.genome = genome
        self.net = net
    
    def draw(self, screen):
        #pygame.draw.rect(screen, (255,0,0), self.rect)
        screen.blit(self.text, (self.rect.x, self.rect.y - 20))
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def fall(self):
        self.rect.y += 2

    def jump(self):
        self.rect.y -= 20
        self.isJump += 20

    def collision(self, wall):
        if self.rect.y < -1:
            return 1
        if self.rect.y > 480:
            return 1
        return self.rect.colliderect(wall)

    def update(self):
        if self.alive == 1:
            if self.isJump > 0 and self.isJump <= 100:
                self.jump()
            else:
                self.isJump = 0
                self.fall()

    def create_img(self, file):
        image = pygame.image.load(file).convert()
        image = pygame.transform.scale(image, (70, 50))
        return image

    def animation(self, img):
        if img == 0:
            self.image = self.create_img("assets/redbird-down.png")
        else:
            self.image = self.create_img("assets/redbird-upflap.png")

    def update_score(self, wall, pos_x):
        if (wall.rect.x == pos_x and self.alive == 1):
            self.score += 1
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render(f'{self.score}', True, (0, 0, 0))

    def died(self):
        self.alive = 0