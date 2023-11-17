from pygame.sprite import Sprite

class Button(Sprite):
    def __init__(self, group, main, image):
        super().__init__(group)
        main.add(self)
        self.image = image
        self.rect = self.image.get_rect()

    def press(self):
        pass

    def remove(self):
        self.rect.x = 2000
        self.rect.y = 2000

    def im_change(self, im):
        self.image = im
