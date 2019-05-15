import pygame
import os


class Game:
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.win = pygame.display.set_mode((self.witdh,self.height))
        self.enemies = []
        self.towers = []
        self.money = 100
        self.lives = 10
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        pygame.display.update()