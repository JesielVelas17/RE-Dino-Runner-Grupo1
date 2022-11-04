import pygame

from dino_runner.component.heart.life import Life
from dino_runner.component.heart.life import Life
from dino_runner.component.heart.life_manager import LifeManager
from dino_runner.component.ornaments.cloud import Cloud
from dino_runner.component.power_up.hammer import Hammer
from dino_runner.component.power_up.hammer_power_up import HammerPowerUp
from dino_runner.utils import text_utils
from dino_runner.component.power_up.power_up_manager import PowerUpManager
from dino_runner.component.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITTLE, FPS, numbers_life,HAMMERS
from dino_runner.component.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.life = Life()
        self.life_manager = LifeManager()
        self.hammer = Hammer()
        self.hammer_manager = HammerPowerUp()
        self.cloud = Cloud()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.lifes = numbers_life
        self.speed_hammer = 20
        self.power_hammer=False
        self.number_hammer=HAMMERS
        self.tomo_martillo=False

    def score(self):
        self.points += 1
        if self.points % 20 == 0:
            self.game_speed += 0.5
        elif self.points % 1000 == 50:
            self.game_speed = 20
        score_element, score_element_rec = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rec)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        half_width = SCREEN_WIDTH // 2
        half_height = SCREEN_HEIGHT // 2
        if self.death_count == 0:
            text_element, text_element_rec = text_utils.get_centered_message('Press any key to Start ')
            self.screen.blit(text_element, text_element_rec)
        elif self.death_count >= 1:
            text_element, text_element_rec = text_utils.get_centered_message('Press any key to Restart ')
            self.screen.blit(text_element, text_element_rec)
            text_element, text_element_rec = text_utils.get_centered_message('Death count :' + str(self.death_count),
                                                                             height=half_height + 40)
            self.screen.blit(text_element, text_element_rec)
            text_element, text_element_rec = text_utils.get_centered_message('Points :' + str(self.points),
                                                                             height=half_height + 80)
        self.screen.blit(text_element, text_element_rec)
        self.screen.blit(ICON, (half_width - 40, half_height - 150))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        self.points = 0
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()
                self.lifes = numbers_life  # resetea nro de vidas
                self.player.resettype()  # cuando se muere resetea al dino
                self.reset_game() #resetea la velocidad
                self.power_up_manager.reset_hammers()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        self.screen.fill((255, 255, 255))

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_hammer,self.tomo_martillo=self.power_up_manager.update(self.points, self.game_speed, self.player, user_input)
        self.number_hammer=self.power_up_manager.lanzar_hammer(user_input,self.power_hammer,self.player)
        self.cloud.update(self.game_speed)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.cloud.draw(self.screen)

        for x in range(0, self.lifes):  # dibujamos el numero de vidas que queremos
            self.life.draw(self.screen)  # dibuja el corazon
            self.life.coordinates(self.lifes)  # actualizamos las coordenadas
        if (self.tomo_martillo==True):
            for x in range(0, self.number_hammer):  # dibujamos el numero de vidas que queremos
                self.hammer.draw_hammer(self.screen)  # dibuja el martillo
                self.hammer.coordinates(self.number_hammer)  # actualizamos las coordenadas
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def reset_game(self):
        self.game_speed=20
