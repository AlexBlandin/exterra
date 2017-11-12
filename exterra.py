import pygame, os
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
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (500, 100) #Set initial window position
    pygame.init()
    width, height = 933, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("ExTerra")


    #
    ##  Physics Setup
    #
    framerate = 60 #60FPS #PCMasterRace #FrameRatePolice
    clock = pygame.time.Clock()


    #
    ##  Background Setup
    #
    image_background = True

    if image_background:
        background, background_rect = import_image("mountain.jpg")
        screen.blit(background, background_rect)
    else:
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

    #Some text rendering
    title = text_image("ExTerra", 36, (10, 10, 10))
    subtitle = text_image("An Alex Blandin & William Webb 4X Space Game", 28, (10, 10, 10))

    #Set text positions
    titlepos = title.get_rect(centerx = background.get_width()/2)
    subtitlepos = subtitle.get_rect(centerx = background.get_width()/2, centery = 35)

    #Showing it can blit to the background
    background.blit(title, titlepos)
    background.blit(subtitle, subtitlepos)

    #Some graph rendering
    graph = graph_image(linear_plot(graph_size = [3, 3], points = [3, 2, 7]))
    background.blit(graph, (533, 500))

    screen.blit(background, (0, 0))


    #
    ##  Setting up the save data -- and testing it for now
    #
    save = Save()
    save.load()

    #checking save works
    print(save.__dict__) #print all of its members
    save.playername = "Alex"
    save.playertime += 1
    save.save()
    if save.playertime >= 4:
        save.clear()

    #checking Singletons work
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
        clock.tick(framerate) #if we want a static framerate

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

        for e in entities: #draw everything
            e.update()
            screen.blit(e.image, e.rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__': main()
