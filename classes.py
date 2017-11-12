import pygame, pickle
from filehandling import *
from singleton import *

#
##  Base Class -- just something that gets rendered
#
class Entity (pygame.sprite.Sprite):
    def __init__(self, image, x = 0, y = 0, colourKey = None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = import_image(image, colourKey)
        self.original, scratch = import_image(image, colourKey)
        self.rect = self.rect.move(x, y)

    def center(self):
        self.rect[0] -= int( self.rect[2] / 2 )
        self.rect[1] -= int( self.rect[3] / 2 )

    def flip():
        self.image = pygame.transform.flip(self.image, 1, 0)

    def rotate(self, angle):
        center = self.rect.center
        angle %= 360
        if angle == 0:
            self.image = self.original
        else:
            self.image = pygame.transform.rotate (self.original, angle)
        self.rect = self.image.get_rect(center=center)

    def update(self):
        pass


#
##  Menu -- singleton representing all screens in the game -- woot woot data-oriented design
#
@Singleton
class Menu (Entity):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.original = None, None

    def addtext(self, image, x, y): #offset to the menu's position
        pass

    def somecombinationofalldata():
        return None

    def update(self):
        pass


#
##  Save data -- for now all data is stored in here when saving/loading
#
@Singleton
class Save():
    def __init__ (self):
        self.playertime = 0

    def save (self):
        with open("save.pkl", "wb") as p:
            pickle.dump(self.__dict__, p, pickle.HIGHEST_PROTOCOL)

    def load (self):
        try:
            with open("save.pkl", "rb") as p:
                self.__dict__.update(pickle.load(p))
        except:
            self.save()

    def clear (self):
        self.__dict__ = {}
        self.__init__()
        self.save()


#
##  "Physics" enabled entities
#
class PhysEntity (Entity):
    def __init__(self, image, x = 0, y = 0, speed = (0, 0), colourKey = None):
        Entity.__init__(self, image, x, y, colourKey)
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
