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
    context["screen_width"], context["screen_height"] = 900, 900
    screen = pygame.display.set_mode((context["screen_width"], context["screen_height"]))
    pygame.display.set_caption("Caption")


    #
    ##  Image imports
    #
    images["stars.png"] = import_image("stars.png")

    #
    ##  Physics Setup
    #
    framerate = 60 #60FPS #PCMasterRace #FrameRatePolice
    clock = pygame.time.Clock()
    context["leftdown"] = False


    #
    ##  Initialise any static images based on screen-size etc.
    #
    basecolour = pygame.Surface((context["screen_width"], context["screen_height"]))
    basecolour = basecolour.convert()
    basecolour.fill((250, 250, 250))
    images["basecolour"] = basecolour




    #
    ##  Pretty screens here
    #
    def solarsystem():
        print("A pretty picture of the solar system")

    def research():
        print("Some nice research statistics and options")

    menu = {0 : solarsystem,
            1 : research
    }
    currentmenu = 0



    #
    ##  Setting up the save data -- and testing it for now
    #
    save = Save()
    ingame = False


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
        if not running:
            continue

        #mouse https://www.pygame.org/docs/ref/mouse.html
        context["leftwaspressed"] = context["leftdown"]
        context["leftdown"], context["rightdown"], context["middledown"] = pygame.mouse.get_pressed()
        context["mousepos"] = pygame.mouse.get_pos() # -> (x, y)
        if context["leftdown"] and not context["leftwaspressed"]:
            context["leftpressed"] = True
        else:
            context["leftpressed"] = False

        #for now not "zeroing" the screen, relying on background being sufficiently large, otherwise will need to use coloured fill to start frame
        currentbackground = "stars.png"
        blitque = [(images[currentbackground], (0, 0))] #refresh blitque with the background


        #Some text rendering
        title, titlerect = text_box("ExTerra", fontsize = 36, fontcolour = (150, 150, 150))
        subtitle = text_image("A William Webb & Alex Blandin 4X Space Game", 28, (120, 120, 120))

        #Set text positions
        titlerect = title.get_rect(centerx = context["screen_width"] / 2, y = 5)
        subtitlerect = subtitle.get_rect(centerx = context["screen_width"] / 2, centery = 50)

        #Showing it can blit to the background
        blitque.append((title, titlerect))
        blitque.append((subtitle, subtitlerect))

        if ingame:
            menu[currentmenu] #say, 0 or 1 or 2 etc.

        else:
            pressed, newgame = button(text = "New Game", centerx = context["screen_width"] / 2, centery = 100, width = 108, height = 50, colour = (200, 200, 200), fontsize = 28, fontcolour = (10, 10, 10))
            if pressed:
                save.clear()
                print("New game")
                ingame = True
                currentmenu = 0
                #move to game state.
                #Redraw the frame with the maps and buttons.
                #open tutorial? We'll need to make some class to give the first instructions on how to interact with the interface.
            blitque.append(newgame)

            pressed, loadgame = button(text = "Load Game", centerx = context["screen_width"] / 2, centery = 175, width = 108, height = 50, colour = (200, 200, 200), fontsize = 28, fontcolour = (10, 10, 10))
            if pressed:
                save.load()
                print("Load game")
                ingame = True
                currentmenu = 0
                #give up the launch codes
                #Load the previous game state. Menus should be closed.
            blitque.append(loadgame)

            pressed, quitgame = button(text = "Fuck this Gay Earth", centerx = context["screen_width"] / 2, centery = 250, width = 108, height = 50, colour = (200, 200, 200), fontsize = 28, fontcolour = (10, 10, 10))
            if pressed:
                print("Quit Game")
                running = False
            blitque.append(quitgame)


        for image, rect in blitque: #blit straight to screen -- can do by layer IF NEEDED, would start with background & move forward
            screen.blit(image, rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__': main()
