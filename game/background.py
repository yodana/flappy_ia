import pygame
from PIL import Image

class Background:
    def __init__(self, w, h):
        self.background = self.construct_background(w, h)

    def update(self, wall, pos_x):
        pass

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

    def construct_background(self, w, h):
        image = Image.open('assets/background.png')
        new_image = image.resize((w + 100, h + 100))
        new_image.save('assets/background_resize.png')
        return pygame.image.load("assets/background_resize.png").convert()
