from settings import *
from cookie import Cookie


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1600, 900))
        pygame.display.set_caption("Cookie Clicker")

        self.new_font = pygame.font.Font(None, 50)
        self.clock = pygame.time.Clock()

        self.bg_surface = pygame.image.load(
            join("graphics", "cookie-clicker-background.jpg")
        ).convert()

        self.cookie = Cookie()
        self.clicked_cookie = False

    def check_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.cookie.cookie_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked_cookie = True
            else:
                if self.clicked_cookie:
                    self.cookie.cookies_clicked += 1
                    self.clicked_cookie = False

    # event loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            text_surface = self.new_font.render(
                f"You have currently clicked {self.cookie.cookies_clicked} cookies",
                True,
                "white",
            )

            self.screen.blit(self.bg_surface, (0, 0))
            self.screen.blit(text_surface, (500, 50))

            self.cookie.draw()
            self.check_collision()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    main = Main()
    main.run()
