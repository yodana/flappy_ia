import pygame
from player import Player
from wall import Wall
from score import Score
from background import Background
import neat
import os

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.background = Background(640, 480)
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = []
        self.score = Score()
        self.walls = []
        self.size = 0
        self.state = 1
        self.anim = 0
        pygame.time.set_timer(pygame.USEREVENT, 2200)
        pygame.time.set_timer(pygame.USEREVENT + 1, 500)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.walls.append(Wall(self.screen.get_width(), self.size))
                self.size = 0 if self.size > 0 else self.screen.get_height()
            if event.type == pygame.USEREVENT + 1:
                for p in self.player:
                    p.animation(self.anim)
                self.anim = 1 if self.anim == 0 else 0
                 
            if event.type == pygame.KEYDOWN:
                if event.key == 32 and self.state == 1:
                    pass
                    #self.player.jump()
                if event.key == 27:
                    self.running = False
                if event.key == 122 and self.state == 0:
                    self.reinit()
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if self.state == 1:
            for p in self.player:
                if p.alive == 1:
                    p.update()
            for wall in self.walls:
                wall.update()
                for p in self.player:
                    if p.alive == 1:
                        p.update_score(wall, p.rect.x)
                        if p.collision(wall.rect) == True:
                            p.died()
                    #self.state = 0
            self.walls = [wall for wall in self.walls if not wall.isOut()]
        if self.state == 0:
            self.score.final()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.background.draw(self.screen)
        for p in self.player:
            if p.alive == 1:
                p.draw(self.screen)
        for wall in self.walls:
            wall.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()

    def reinit(self):
        self.state = 1
        self.walls = []
        self.player = []

    def train_ia(self, genomes, config):
        net = []
        for i, genome in genomes:
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            self.player.append(Player(100, 150, genome, net))
        self.running = 1
        while self.running:
            self.event_handler()
            buttom = 0
            top = 0
            x_wall = 0
            position_y = 0
            if len(self.walls) > 1:
                wall = [wall for wall in self.walls if wall.rect.x > 70]
                x_wall = wall[0].x
                position_y = wall[0].y
                if wall[0].y == 0:
                    buttom = wall[0].y
                    top = wall[0].y + wall[0].height
                else:
                    top = wall[0].y - wall[0].height
                    buttom = wall[0].y
            count = 0
            for p in self.player:
                if p.alive == 0:
                    count += 1
                if count == len(self.player):
                    self.running = 0
                if p.alive == 1:
                    p.score = p.score + 1
                    
                    output = p.net.activate((p.rect.y, abs(p.rect.y - top), abs(p.rect.y - buttom), abs(p.rect.x - x_wall), position_y))
                    if output[0] > 0.5:
                        p.jump()
                    p.genome.fitness = p.score
            self.update()
            self.draw()
            self.clock.tick(60)

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.draw()
            self.clock.tick(60)

def eval_genomes(genomes, config):
    game.train_ia(genomes, config)
    game.reinit()

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.Checkpointer(generation_interval=50, filename_prefix='neat-checkpoint-'))
    pygame.init()
    game = Game()
    winner = p.run(eval_genomes, 1000)