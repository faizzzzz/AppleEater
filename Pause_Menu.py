import pygame, time
import Basics as sb
# import Reset
# from Apple import apple
from message import message_display


class PauseMenu:
    def __init__(self):
        self.isGamePaused = False   # check to see if the game is paused or not.
        self.showMenu = True        # check to see if the menu has to be displayed or not.
        self.gameRun = False        # check to see if the game has to run or not.
        self.textWelcome = "Welcome"
        self.textOptions = "press Enter to start or Esc to exit"
        self.winningPoints = sb.winningPoints

    def menu(self):
        sb.gameDisplay.fill(sb.white)
        
        # the start meny of the game
        message_display("Welcome", sb.xres/2, sb.yres/2 - 50, 30, sb.gameDisplay)
        message_display("Press Enter to start or Esc to exit.", sb.xres/2, sb.yres/2 - 100, 25, sb.gameDisplay)
        message_display("Instructions: Whoever collects " + str(sb.winningPoints) + " apples first, wins. Use arrow keys to navigate.", sb.xres/2, sb.yres/2, 20, sb.gameDisplay)
        message_display("Press 'P' to pause and 'Enter' to continue.", sb.xres/2, sb.yres/2 + 25, 20, sb.gameDisplay)
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.showMenu == True:
                    # if the player presses enter, the menu is no longer displayed and the game starts.
                    self.showMenu = False
                    self.gameRun = True

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

Menu = PauseMenu()
