from pygame.sprite import Group
from pygame.sprite import Sprite

from Git.settings import *
from Git.utils import load_image

pygame.init()
screen = pygame.display.set_mode(size)
players = [(20, 150), (20, 400)]
all_sprites = Group()
cars = Group()
utility = Group()
win_img = Group()
CAR_SPEED = 0.01
IDLE_a = -0.00001
CLICK_a = 0.003


def win(p_number):
    EndWindow(f"race_end_{p_number}.png")


def reset():
    global all_sprites, cars, utility, win_img, p1, p2, start, finish
    all_sprites = Group()
    cars = Group()
    utility = Group()
    win_img = Group()
    p1, p2 = Car(1), Car(2)
    start, finish = StartAndFinish("start"), StartAndFinish("finish")


class Car(Sprite):
    def __init__(self, player_number):
        super().__init__(all_sprites, cars)
        self.pos = players[player_number - 1]
        self.image = load_image(f"race_cars{player_number}.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.vx = CAR_SPEED
        self.player_number = player_number

    def update(self):
        self.vx += IDLE_a
        if self.vx < 0:
            self.vx = 0
        self.pos = self.pos[0] + self.vx, self.pos[1]
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])
        if pygame.sprite.spritecollideany(self, utility):
            sprite = pygame.sprite.spritecollideany(self, utility)
            if sprite.tp == "finish":
                self.vx = 0
                win(self.player_number)

    def speed_change(self):
        self.vx += CLICK_a


class StartAndFinish(Sprite):
    def __init__(self, tp):
        super().__init__(all_sprites, utility)
        self.image = load_image(f"race_{tp}.png")
        self.rect = self.image.get_rect()
        self.tp = tp
        if tp == "start":
            self.rect.x, self.rect.y = 2, 0
        elif tp == "finish":
            self.rect.x, self.rect.y = 720, 0


class EndWindow(Sprite):
    def __init__(self, image):
        super().__init__(all_sprites, win_img)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = 180
        self.rect.y = 230


p1, p2 = Car(1), Car(2)
start, finish = StartAndFinish("start"), StartAndFinish("finish")

reset()


def race_run(key_one, key_two):
    PLAYERONEKEY = key_one
    PLAYERTWOKEY = key_two
    pygame.display.set_caption("race")
    reset()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == PLAYERONEKEY:
                    p1.speed_change()
                elif event.key == PLAYERTWOKEY:
                    p2.speed_change()
                elif event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill((5, 205, 45))
        all_sprites.update()
        utility.draw(screen)
        cars.draw(screen)
        win_img.draw(screen)
        pygame.display.flip()
