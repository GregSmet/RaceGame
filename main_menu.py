from pygame.sprite import Group

from button import *
from race import race_run
from settings import *
from utils import load_image

pygame.init()
screen = pygame.display.set_mode(size)
# sprite groups
all_sprites = Group()
games = Group()
setting_btns = Group()
pygame.display.set_caption('Menu')

# window control vars
running = True
setting_open = False
volume_on = True
button_registration = 0
new_btn = None


# These funcs are creating only to paste them into button classes, so they are with no any specific title
def e():
    print("race")
    race_run(PLAYERONEKEY, PLAYERTWOKEY)
    pygame.display.set_caption("Menu")


def sett():
    global setting_open
    setting_open = not setting_open


def btn_change(player):
    global button_registration
    button_registration = player
    if button_registration == 1:
        first_btn.im_change(
            print_key('button_red.png', size_of_button, 'change'))
    elif button_registration == 2:
        second_btn.im_change(
            print_key('button_blu.png', size_of_button, 'change'))


def btn_new():
    global button_registration
    global PLAYERONEKEY
    global PLAYERTWOKEY
    if button_registration == 1:
        if PLAYERTWOKEY != new_btn:
            PLAYERONEKEY = new_btn
        first_btn.im_change(
            print_key('button_red.png', size_of_button, PLAYERONEKEY))
    elif button_registration == 2:
        if PLAYERONEKEY != new_btn:
            PLAYERTWOKEY = new_btn
        second_btn.im_change(
            print_key('button_blu.png', size_of_button, PLAYERTWOKEY))
    button_registration = 0


def print_key(image_name, size_of_button, key):
    image = pygame.transform.scale(load_image(image_name), size_of_button)
    font = pygame.font.SysFont('arial', 30)
    text = font.render(keys[key], False, 'black')
    text_x = image.get_rect().w // 2 - text.get_width() // 2
    text_y = image.get_rect().h // 2 - text.get_height() // 2
    image.blit(text, (text_x, text_y))
    return image


race = Button(games, all_sprites, pygame.transform.scale(load_image("race.png"), (350, 350)))
race.press = e

settings = Button(games, all_sprites, pygame.transform.scale(load_image("gear.png"), (64, 64)))
settings.press = sett

settings_back = Button(setting_btns, all_sprites, pygame.transform.scale(load_image("back_button.png"), (128, 64)))
settings_back.press = sett

first_btn = Button(setting_btns, all_sprites, print_key('button_red.png', size_of_button, PLAYERONEKEY))
first_btn.press = lambda: btn_change(1)
second_btn = Button(setting_btns, all_sprites, print_key('button_blu.png', size_of_button, PLAYERTWOKEY))
second_btn.press = lambda: btn_change(2)

race.rect = race.rect.move(100, 100)

settings.rect = settings.rect.move(400 - 32, 500)
settings_back.rect = settings_back.rect.move(64, HEIGHT - 128)
first_btn.rect = first_btn.rect.move(150, 200)
second_btn.rect = second_btn.rect.move(WIDTH - 150 - 128, 200)

# initializing settings

# main cycle
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if setting_open and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            setting_open = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if not setting_open:

                for b in games.sprites():
                    if b.rect.collidepoint(x, y):
                        b.press()
                        break
            else:

                for b in setting_btns.sprites():
                    if b.rect.collidepoint(x, y):
                        b.press()
                        break
        else:
            if button_registration:
                if event.type == pygame.KEYDOWN:
                    new_btn = event.key
                    btn_new()

    background_color = (
        background_color[0] + background_multipliers[0] * 0.03, background_color[1] + background_multipliers[1] * 0.05,
        background_color[2] + background_multipliers[2] * 0.07)

    for i in range(3):
        if background_color[i] >= 170 or background_color[i] <= 0:
            background_multipliers[i] *= -1
    screen.fill(background_color)

    if not setting_open:
        games.draw(screen)
        all_sprites.update()
    else:
        setting_btns.draw(screen)
        setting_btns.update()
    pygame.display.update()
pygame.quit()
