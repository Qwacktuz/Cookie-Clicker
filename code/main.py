from settings import *
from math import sin

pygame.init()
new_font = pygame.font.Font(None, 50)
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Cookie Clicker')
clock = pygame.time.Clock()

bg_surface = pygame.image.load(join('graphics', 'cookie-clicker-background.jpg')).convert()
cookie_surface = pygame.image.load(join('graphics', 'cookie.png')).convert_alpha()
cookie_rect = cookie_surface.get_rect(center = (800, 500))

cookies_clicked = 0
clicked_cookie= False

def draw_cookie():
    scale = 1.25 + sin(pygame.time.get_ticks() / 800) / 10
    scaled_surf = pygame.transform.smoothscale_by(cookie_surface, scale)
    scaled_rect = scaled_surf.get_rect(center = (800, 500))
    screen.blit(scaled_surf, scaled_rect)

# event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    text_surface = new_font.render(f'You have currently clicked {cookies_clicked} cookies', True, 'white')

    screen.blit(bg_surface,(0,0))
    screen.blit(text_surface,(500,50))
    draw_cookie()

    mouse_pos = pygame.mouse.get_pos()
    if cookie_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            clicked_cookie = True
        else:
            if clicked_cookie:
                cookies_clicked += 1
                clicked_cookie = False

    pygame.display.update()
    clock.tick(60)