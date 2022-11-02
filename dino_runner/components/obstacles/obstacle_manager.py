import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.birds import Birds
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__ (self):
        self.obstacles = []
        self.option_numbers = list(range(1, 5))

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Birds(BIRD))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, game):
        for obstacle in self.obstacles:
            obstacle.draw(game.screen)