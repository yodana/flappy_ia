import pygame

class Score:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.score = 0
        self.x = 10
        self.y = 10
        self.size = 36
        self.font = pygame.font.Font(None, self.size) # (police, taille)
        self.text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))

    def update(self, wall, pos_x):
        if (wall.rect.x == pos_x):
            self.score += 1
        self.font = pygame.font.Font(None, self.size)
        self.text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))

    def final(self):
        self.font = pygame.font.Font(None, 80)
        self.text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
        self.x = 210
        self.y = 190

    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))