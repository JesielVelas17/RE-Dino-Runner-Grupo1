import pygame.time
import random
import pygame
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, numbers_life
from dino_runner.component.obstacles.cactus import Cactus
from dino_runner.component.obstacles.birds import Birds
from dino_runner.component.obstacles.large_cactus import LargeCactus


class ObstacleManager:
    def __init__ (self):
        self.obstacles = []
        
        self.lifes = numbers_life
        #self.option_numbers = list(range(1, 10))
        self.game_speed = 20

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
                
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Birds(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(self.obstacles, game.game_speed)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)

                elif game.lifes > 1:
                    self.obstacles.remove(obstacle)
                    game.lifes -= 1

                else:
                    game.playing = False
                    game.death_count += 1
                    break
            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):

                if obstacle in self.obstacles:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles =[]
