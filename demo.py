import pygame, os
from pygame.locals import *
from pygame.compat import geterror
if not pygame.font: raise SystemExit("Unable to render text, game unplayable!")
if not pygame.mixer: print ("!!!Warning, sound disabled!!!")

#Our stuff
from filehandling import *
from classes import *
from rendering import *
from exterra import *

images = {}
offset = 0

def demo(background, leftdown, rightdown, middledown, mousepos, screen_width, screen_height, images, framerate, clock, save):
        if button(background, x = 400, y = 350, width = 40, height = 40):
            offset -= 10
        else:
            offset += 0.3

        #Draw a white rect
        rectangle, rectrect = box(x = (screen_width / 2) - 300, y = 0, width = 600, height = 70, colour = (90, 90, 90))
        background.blit(rectangle, rectrect)

        #Some text rendering
        title, titlerect = text_box("ExTerra", fontsize = 36, fontcolour = (70, 70, 70))
        subtitle = text_image("A William Webb & Alex Blandin 4X Space Game", 28, (10, 10, 10))

        #Set text positions
        titlerect = title.get_rect(centerx = screen_width/2, y = 5)
        subtitlerect = subtitle.get_rect(centerx = screen_width/2, centery = 50)

        #Showing it can blit to the background
        background.blit(title, titlerect)
        background.blit(subtitle, subtitlerect)

        #Some graph rendering
        background.blit(images["linegraph"], (533, 300)) #and now we can blit a graph
        background.blit(images["piechart"], (100, 300))

        earth = pygame.transform.scale(images["earth.png"], (256, 256))
        earthrect = earth.get_rect(centerx = screen_width/2, centery = (screen_height/2) + offset)

        background.blit(earth, earthrect)

        screen.blit(background, (0, 0))
