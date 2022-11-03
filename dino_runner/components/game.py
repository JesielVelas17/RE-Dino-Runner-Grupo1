import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.score import Score
from dino_runner.components.ornaments.cloud import Cloud
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SMALL_CACTUS, TITLE, FPS, CLOUD, FONT_STYLE, RUNNING
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.death_count = 0
        self.score = Score()
        self.points = 0
     
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()     

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self, self.score)
        self.cloud.update(self. game_speed) 
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self)
        self.cloud.draw(self.screen)
        self.score.draw(self.screen)
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
        
    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text_component = font.render("Press any key to Start", True, (0,0,0) )
            
        elif self.death_count > 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text_component = font.render("Press any key to Restart", True, (0,0,0) )
            
            text_score = font.render("Your Score: " + str(self.points), True, (0,0,0))
            text_score_rect = text_score.get_rect()
            text_score_rect.center = (half_screen_width, half_screen_height + 40)
            self.screen.blit(text_score, text_score_rect)
            
            text_death = font.render("Death Count: " + str(self.death_count), True, (0,0,0))
            text_death_rect = text_death.get_rect()
            text_death_rect.center = (half_screen_width, half_screen_height + 80)
            self.screen.blit(text_death, text_death_rect)

        text_rect = text_component.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text_component, text_rect) 

        self.screen.blit(RUNNING[0], (half_screen_width -30, half_screen_height -140))
        pygame.display.update()
        self.handle_key_event_on_menu()
        
    def handle_key_event_on_menu (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

