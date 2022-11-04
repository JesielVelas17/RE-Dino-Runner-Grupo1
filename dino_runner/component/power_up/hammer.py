from dino_runner.component.power_up.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, SCREEN_WIDTH, HAMMER_TYPE


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        self.rectx=25
        self.recty=35
        super().__init__(self.image, self.type)

    def move(self, game_speed, moving):
        print("moviendo")
        self.rect.x += game_speed + 5
        print(self.rect.x)
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = -100
            moving.hammer_moving = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def draw_hammer(self,screen):
        screen.blit(self.image, [self.rectx,self.recty])

    def coordinates(self, number_hammer):
        self.rectx += 25  # sumar 25 para que este a lado
        if self.rectx == 25 + 25 * number_hammer:  # si llega a el nro de corazones,vuelve a imprimir desde el inicio para que se quede quieto en un solo lugar
            self.rectx = 25
