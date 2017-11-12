import pygame
from pygame.locals import *
from pygame.compat import geterror
if not pygame.font: raise SystemExit("Unable to render text, game unplayable!")
if not pygame.mixer: print ("!!!Warning, sound disabled!!!")


#Our stuff
from filehandling import *
from classes import *
from rendering import *


def main():

    #
    ##  Window Setup
    #
    pygame.init()
    width, height = 933, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("ExTerra")

    #
    ##  Physics Setup
    #
    framerate = 60 #60FPS #PCMasterRace #FrameRatePolice
    clock = pygame.time.Clock()

    image_background = True

    if image_background:
        background, background_rect = import_image("mountain.jpg")
        screen.blit(background, background_rect)
    else:
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))


    #
    ##  Create Text Images -- for screens etc
    #

    #Titles
    title = make_text("ExTerra", 36, (10, 10, 10))
    titlepos = title.get_rect(centerx=background.get_width()/2)

    subtitle = make_text("An Alex Blandin & William Webb 4X Space Game", 28, (10, 10, 10))
    subtitlepos = subtitle.get_rect(centerx=background.get_width()/2, centery = 35)


    #Adding to background for now
    background.blit(title, titlepos)
    background.blit(subtitle, subtitlepos)

    screen.blit(background, (0, 0))

    #
    ##  Setting up the save data -- and testing it for now
    #
    save = Save()
    save.load()
    print(save.__dict__) #print all of its members
    save.playername = "Alex"
    save.playertime += 1
    save.save()
    if save.playertime >= 4:
        save.clear()

    #checking Singletons
    menu = Menu()
    hayo = Menu()
    mayo = Menu()

    print("It is %s that Menu() is a Singleton" % (menu is hayo is mayo))


    #
    ##  Entity Setup
    #
    entities = []
    player = Entity("player.png", int( width / 2 ), int( height / 2 ))
    entities.append(player) #player is passed as a pointer
    player.center()


    #
    ##  Main Loop
    #
    running = True
    while running:
        clock.tick(framerate)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                break
            elif event.type == MOUSEBUTTONDOWN:
                pass
            elif event.type == MOUSEBUTTONUP:
                pass
        if not running:
            continue
        
        screen.blit(background, (0, 0))

        for e in entities: #draw entities
            e.update()
            screen.blit(e.image, e.rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__': main() #ignore this, pygame likes to cry
