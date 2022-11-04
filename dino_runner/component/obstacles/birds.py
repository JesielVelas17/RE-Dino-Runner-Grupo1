import random
from dino_runner.component.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Birds(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(260, 320)
        self.index = 0
        
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1