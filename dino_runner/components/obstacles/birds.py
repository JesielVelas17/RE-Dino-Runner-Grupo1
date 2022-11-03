import random

from .obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Birds(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = random.randint(250, 300)
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.images[self.index // 5], self.rect)
        self.index += 1