import pygame, os
from pygame.locals import *
from pygame.compat import geterror
if not pygame.font: raise SystemExit("Unable to render text, game unplayable!")
if not pygame.mixer: print ("!!!Warning, sound disabled!!!")

#Our stuff
import globals
globals.init()
from globals import *

from filehandling import *
from classes import *
from rendering import *



def main():
    #
    ##  Window Setup
    #
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (500, 100) #Set initial window position
    pygame.init()
    context["screen_width"], context["screen_height"] = 1920, 1080
    screen = pygame.display.set_mode((context["screen_width"], context["screen_height"]))
    pygame.display.set_caption("Exterra: a 4X Game")


    #
    ## Background images
    #

    images["stars.png"] = import_image("stars.png")

    #Include the various images for the New Game, Load Game, Quit.

    #
    ## Physics
    #

    framerate = 60
    clock = pygame.time.Clock()

    #
    ## Buttons for save, load, quit.
    #

    #
    ## Menu loop
    #

    while running:
        clock.tick(framerate)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                break
            if not running:
                continue

            #mouse https://www.pygame.org/docs/ref/mouse.html
            #pygame.event.wait() or pygame.event.get() and check all of those events
            context["leftdown"], context["rightdown"], context["middledown"] = pygame.mouse.get_pressed() # -> (mouse1, mouse2, mouse3) -- a sequence of bools, true = pressed
            context["mousepos"] = pygame.mouse.get_pos() # -> (x, y)
            #pygame.mouse.set_pos()
            #pygame.mouse.set_visible()
            #pygame.mouse.get_focused()

            currentbackground = "stars.png"
            blitque = [(image[currentbackground], (0,0))]

            title, titlerect = text_box("ExTerra", fontsize = 36, fontcolour = (70, 70, 70))
            subtitle = text_image("A William Webb & Alex Blandin 4X Space Game", 28, (10, 10, 10))


            for image, rect in blitque: #blit straight to screen -- can do by layer IF NEEDED, would start with background & move forward
                screen.blit(image, rect)

            pygame.display.flip()

        pygame.quit()
