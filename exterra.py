import pygame, os
from pygame.locals import *
from pygame.compat import geterror
if not pygame.font: raise SystemExit("Unable to render text, game unplayable!")
if not pygame.mixer: print ("!!!Warning, sound disabled!!!")

#Our stuff
from filehandling import *
from classes import *
from rendering import *
from demo import *

def main():
    #
    ##  Window Setup
    #
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (500, 100) #Set initial window position
    pygame.init()
    screen_width, screen_height = 933, 900
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Caption")
    context = Context()
    context.screen = screen
    context.screen_width = screen_width
    context.screen_height = screen_height


    #
    ##  Image imports
    #
    images = {}
    context.images = images

    images["earth.png"] = import_image("earth.png", -1)
    images["mountain.jpg"] = import_image("mountain.jpg")
    images["player.png"] = import_image("player.png")
    some_data_plot = linear_plot([3, 1, 2, 7], size_in_inches = [3, 3]) #plot the points, optional arguments after
    images["linegraph"] = graph_image(some_data_plot) #generate an image pygame understands
    images["piechart"] = graph_image(pie_chart([3.14159, 6.28318], labels = ["pi", "tau"], shadow = True, size_in_inches = [3.14, 3.14]))


    #
    ##  Physics Setup
    #
    framerate = 60 #60FPS #PCMasterRace #FrameRatePolice
    clock = pygame.time.Clock()
    context.framerate = framerate
    context.clock = clock


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
    shave = Save()
    cave = Save()

    print("It is %s that Save() is a Singleton" % (save is shave is cave))


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

        #mouse https://www.pygame.org/docs/ref/mouse.html
        #pygame.event.wait() or pygame.event.get() and check all of those events
        leftdown, rightdown, middledown = pygame.mouse.get_pressed() # -> (mouse1, mouse2, mouse3) -- a sequence of bools, true = pressed
        mousepos = pygame.mouse.get_pos() # -> (x, y)
        #pygame.mouse.set_pos()
        #pygame.mouse.set_visible()
        #pygame.mouse.get_focused()


        currentbackground = "mountain.jpg"


        background.blit(images[currentbackground], (0,0))


        context.background, context.leftdown, context.rightdown, context.middledown, context.mousepos, context.images, context.framerate, context.clock  = background, leftdown, rightdown, middledown, mousepos, images

        demo(context)

        for e in entities: #draw everything
            e.update()
            screen.blit(e.image, e.rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__': main()
