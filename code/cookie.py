from settings import *
from math import sin

class Cookie:
    def __init__(self):
        self.cookie_surface = pygame.image.load(join('graphics', 'cookie.png')).convert_alpha()
        self.cookie_rect = self.cookie_surface.get_rect(center = (800, 500))
        self.screen = pygame.display.get_surface()

        self.cookies_clicked = 0

    def draw(self):
        scale = 1.25 + sin(pygame.time.get_ticks() / 800) / 10
        scaled_surf = pygame.transform.smoothscale_by(self.cookie_surface, scale)
        scaled_rect = scaled_surf.get_rect(center = (800, 500))
        self.screen.blit(scaled_surf, scaled_rect)

