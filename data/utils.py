import os
import sys

import pygame


def load_image(name):
    fullname = f"data/images/{os.path.join('', name)}"
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image