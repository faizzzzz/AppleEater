import pygame, time
import Basics as sb
# import Reset
# from Apple import apple
from message import message_display


class PauseMenu:
    def __init__(self):
        self.isGamePaused = False
        self.showMenu = True
        self.gameRun = False
        self.textWelcome = "Welcome"
        self.textOptions = "press Enter to start or Esc to exit"
        self.winningPoints = 10

    def menu(self):
        sb.gameDisplay.fill(sb.white)
        message_display("Welcome", sb.xres/2, sb.yres/2 - 50, 30, sb.gameDisplay)
        message_display("Press Enter to start or Esc to exit.", sb.xres/2, sb.yres/2 - 100, 25, sb.gameDisplay)
        message_display("Instructions: Whoever collects " + str(sb.winningPoints) + " apples first, wins. Use arrow keys to navigate.", sb.xres/2, sb.yres/2, 20, sb.gameDisplay)
        message_display("Press 'P' to pause and 'Enter' to continue.", sb.xres/2, sb.yres/2 + 25, 20, sb.gameDisplay)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.showMenu == True:
                    self.showMenu = False
                    self.gameRun = True

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

Menu = PauseMenu()