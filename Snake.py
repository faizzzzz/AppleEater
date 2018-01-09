import pygame
from Pause_Menu import Menu
from Rotating_Image import rot_center as rot_img
import Basics as sb

class snake:
    def __init__(self):
        self.angle = 0
        self.faceDIR = (1, 0, 0, 0)     #faceUP, faceRIGHT, faceDOWN, faceLEFT. Clockwise rotation
        self.stepINCR = 5       # the speed the player moves.(twice that of the opponent).
        self.xpos = sb.xres/2   # starts from the middle.
        self.ypos = sb.yres/2   
        self.points = 0     # the points of the player.
        self.pointsINCR = 1 #   # the increment in points after eating 1 apple.

    def move(self):
        # To change the direction of the player.
        if Menu.gameRun == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if self.faceDIR[0] == 1 or self.faceDIR[2] == 1:
                            # the player can only face right if it is facing up or down.
                            self.angle = -90
                            self.faceDIR = (0, 1, 0, 0)     # facing right.

                    if event.key == pygame.K_LEFT:
                        if self.faceDIR[0] == 1 or self.faceDIR[2] == 1:
                            # the player can only face left if it is facing up or down.
                            self.angle = 90
                            self.faceDIR = (0, 0, 0, 1)     # facing left.

                    if event.key == pygame.K_UP:
                        if self.faceDIR[1] == 1 or self.faceDIR[3] == 1:
                            # the player can only face up if it is facing right or left.
                            self.angle = 0
                            self.faceDIR = (1, 0, 0, 0)     # facing up.

                    if event.key == pygame.K_DOWN:
                        if self.faceDIR[1] == 1 or self.faceDIR[3] == 1:
                            # the player can only face down if it is facing right or left.
                            self.angle = 180
                            self.faceDIR = (0, 0, 1, 0)     # facing down.

                    if event.key == pygame.K_p:
                        Menu.isGamePaused = True    # to pause the game.

                    if event.key == pygame.K_RETURN and Menu.isGamePaused == True:
                        Menu.isGamePaused = False   # to unpause the game.

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()      # to quit the game.

        self.snakeHead = rot_img(sb.snakeHead, self.angle)
        self.snakeHead_rect = self.snakeHead.get_rect()

    def motion(self):
        if Menu.isGamePaused == False and Menu.gameRun == True:
            # To go up, the y value of the player has to decrease.
            # To go donw, the y value of the player has to increase.
            # To go right, the x value of the player has to increase.
            # To go left, the x value of the player has to decrease.
            self.step = self.stepINCR
            if self.faceDIR[0] == 1:
                self.ypos -= self.step
            if self.faceDIR[1] == 1:
                self.xpos += self.step
            if self.faceDIR[2] == 1:
                self.ypos += self.step
            if self.faceDIR[3] == 1:
                self.xpos -= self.step

        if Menu.isGamePaused == True and Menu.gameRun == True:
            # if the game is paused the player step increment is set to 0, so the player does not move.
            self.step = 0

    def throughWall(self):
        # if snake reaches the wall, it comes through from the other side.
        if self.xpos < -sb.snakeWidth:
            # if it reaches the left wall.
            self.xpos = sb.xres     # the x position is set to xres, so that it comes from the right wall.
        if self.xpos > sb.xres + sb.snakeWidth:
            # if it reaches the left wall.
            self.xpos = -sb.snakeWidth      # the x position is set to negative of the snake width, so that it comes from the left wall.
        if self.ypos > sb.yres:
            # if it reaches the bottom.
            self.ypos = -sb.snakeHeight     # the y position is set to the negative of the snake height, so that it comes from the top.
        if self.ypos < -sb.snakeHeight:
            # if it reaches the top.
            self.ypos = sb.yres     # they y positio is set to the yres, so that it comes from the bottom.

snakePlayer = snake()
