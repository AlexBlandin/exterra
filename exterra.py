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
    pygame.display.set_caption("Caption")


    #
    ##  Image imports
    #
    images = {}
    images["earth.png"] = import_image("earth.png", -1)
    images["mountain.jpg"] = import_image("mountain.jpg")
    images["player.png"] = import_image("player.png")
    some_data_plot = linear_plot([3, 1, 2, 7], size_in_inches = [3, 3]) #plot the points, optional arguments after
    images["linegraph"] = graph_image(some_data_plot) #generate an image pygame understands
    images["piechart"] = graph_image(pie_chart([3.14159, 6.28318], labels = ["pi", "tau"], explode = [0.1, 0], shadow = True, size_in_inches = [3.14, 3.14]))


    #
    ##  Physics Setup
    #
    framerate = 60 #60FPS #PCMasterRace #FrameRatePolice
    clock = pygame.time.Clock()

    offset = 0


    #
    ##  Background Setup
    #
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))


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


    #
    ##  Main Loop
    #
    running = True
    while running:
        clock.tick(framerate) #if we want a static framerate

        offset += 0.3

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                break
            elif event.type == MOUSEBUTTONDOWN:
                offset -= 0.3
            elif event.type == MOUSEBUTTONUP:
                pass
        if not running:
            continue

        #mouse https://www.pygame.org/docs/ref/mouse.html
        #pygame.event.wait() or pygame.event.get() and check all of those events
        leftdown, rightdown, middledown = pygame.mouse.get_pressed() # -> (mouse1, mouse2, mouse3) -- a sequence of bools, true = pressed
        mousepos = pygame.mouse.get_pos() # -> (x, y)

        if leftdown:
            offset -= 1.0

        #pygame.mouse.set_pos()
        #pygame.mouse.set_visible()
        #pygame.mouse.get_focused()

        currentbackground = "mountain.jpg"


        background.blit(images[currentbackground], (0,0))
        screen_width = background.get_width()
        screen_height = background.get_height()

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

        for e in entities: #draw everything
            e.update()
            screen.blit(e.image, e.rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__': main()
