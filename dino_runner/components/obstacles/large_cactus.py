import random
from .obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS

class LargeCactus(Obstacle):
   def __init__(self, images):
       self.type = random.randint(0,2)
       super().__init__(images, self.type)
       self.rect.y = 300
