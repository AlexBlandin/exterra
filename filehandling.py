import os, pygame
from context import *
from pygame.locals import *
from pygame.compat import geterror

#
##  Directories
#
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

#
##  Return full path to a file
#
def path(name):
    return os.path.join(data_dir, name)


#
##  Return an image and its rect()
#
def import_image(name, colorkey = None):
    image_dir = path(name)

    try:
        image = pygame.image.load(image_dir)
    except pygame.error:
        print ("Failed to import %s " % image_dir)
        raise SystemExit(str(geterror()))

    image = image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)

    return image

#
##  Always returns an object of some form, however if sounds can't be played then it's just a dummy
#
def import_sound(name):
    class NoSound: #dummy for when pygame.mixer fails
        def play(self): pass

    if not pygame.mixer or not pygame.mixer.get_init(): return NoSound() #return dummy

    sound_dir = path(name)

    try:
        sound = pygame.mixer.Sound(sound_dir)
    except pygame.error:
        print("Failed to import %s" % sound_dir)
        raise SystemExit(str(geterror()))

    return sound
