import pygame
from player import Player
from wall import Wall

class Game:
    
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(100, 150)
        self.walls = []
        self.size = 0
        self.state = 1
        pygame.time.set_timer(pygame.USEREVENT, 1500)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.walls.append(Wall(self.screen.get_width(), self.size))
                self.size = 0 if self.size > 0 else self.screen.get_height()
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    self.player.jump()
                if event.key == 27:
                    self.running = False
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if self.state == 1:
            self.player.update()
            for wall in self.walls:
                wall.update()
                if self.player.collision(wall.rect) == True:
                    self.state = 0
            self.walls = [wall for wall in self.walls if not wall.isOut()]

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.player.draw(self.screen)
        for wall in self.walls:
            wall.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.draw()
            self.clock.tick(60)

pygame.init()
game = Game()
game.run()