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
    context["screen_width"], context["screen_height"] = 933, 900
    screen = pygame.display.set_mode((context["screen_width"], context["screen_height"]))
    pygame.display.set_caption("Caption")


    #
    ##  Image imports
    #
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


    #
    ##  Initialise any static images based on screen-size etc.
    #
    basecolour = pygame.Surface((context["screen_width"], context["screen_height"]))
    basecolour = basecolour.convert()
    basecolour.fill((250, 250, 250))
    images["basecolour"] = basecolour


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
    maze = Save()
    endoftheuniverse = Save()
    context["offset"] = 0

    print("It is %s that Save() is a Singleton" % (save is maze is endoftheuniverse))


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
        context["leftdown"], context["rightdown"], context["middledown"] = pygame.mouse.get_pressed() # -> (mouse1, mouse2, mouse3) -- a sequence of bools, true = pressed
        context["mousepos"] = pygame.mouse.get_pos() # -> (x, y)
        #pygame.mouse.set_pos()
        #pygame.mouse.set_visible()
        #pygame.mouse.get_focused()


        #for now not "zeroing" the screen, relying on background being sufficiently large, otherwise will need to use coloured fill to start frame
        currentbackground = "mountain.jpg"
        blitque = [(images[currentbackground], (0, 0))] #refresh blitque with the background




        #Draw a white rect
        rectangle, rectrect = box(x = (context["screen_width"]/2) - 300, y = 0, width = 600, height = 70, colour = (90, 90, 90))
        blitque.append((rectangle, rectrect))

        #Some text rendering
        title, titlerect = text_box("ExTerra", fontsize = 36, fontcolour = (70, 70, 70))
        subtitle = text_image("A William Webb & Alex Blandin 4X Space Game", 28, (10, 10, 10))

        #Set text positions
        titlerect = title.get_rect(centerx = context["screen_width"]/2, y = 5)
        subtitlerect = subtitle.get_rect(centerx = context["screen_width"]/2, centery = 50)

        #Showing it can blit to the background
        blitque.append((title, titlerect))
        blitque.append((subtitle, subtitlerect))

        #Some graph rendering
        blitque.append((images["linegraph"], (533, 300))) #and now we can blit a graph
        blitque.append((images["piechart"], (100, 300)))

        #Generate a more managable Earth. Might be impossible
        earth = pygame.transform.scale(images["earth.png"], (256, 256))
        earthrect = earth.get_rect(centerx = context["screen_width"]/2, centery = (context["screen_height"]/2) + context["offset"])

        blitque.append((earth, earthrect))

        clicked = within(context["mousepos"], earthrect)
        if clicked and context["leftdown"]:
            context["offset"] -= 1


        clicked, buttonpair = button(x = 700, y = 700, width = 100, height = 100, colour = (200, 200, 200))
        if clicked:
            image, rect = buttonpair
            image.fill((170, 170, 170))
            buttonpair = image, rect
        blitque.append(buttonpair)





        for image, rect in blitque: #blit straight to screen -- can do by layer IF NEEDED, would start with background & move forward
            screen.blit(image, rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__': main()
