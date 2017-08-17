import pygame
from Pause_Menu import Menu
from Rotating_Image import rot_center as rot_img
import Basics as sb

class snake:
    def __init__(self):
        self.angle = 0
        self.faceDIR = (1, 0, 0, 0)     #faceUP, faceRIGHT, faceDOWN, faceLEFT
        self.stepINCR = 5
        self.xpos = sb.xres/2
        self.ypos = sb.yres/2
        self.points = 0
        self.pointsINCR = 1
        self.isGameEnd = False
        self.isScore = False

    def move(self):
        if Menu.gameRun == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if self.faceDIR[0] == 1 or self.faceDIR[2] == 1:
                            self.angle = -90
                            self.faceDIR = (0, 1, 0, 0)

                    if event.key == pygame.K_LEFT:
                        if self.faceDIR[0] == 1 or self.faceDIR[2] == 1:
                            self.angle = 90
                            self.faceDIR = (0, 0, 0, 1)

                    if event.key == pygame.K_UP:
                        if self.faceDIR[1] == 1 or self.faceDIR[3] == 1:
                            self.angle = 0
                            self.faceDIR = (1, 0, 0, 0)

                    if event.key == pygame.K_DOWN:
                        if self.faceDIR[1] == 1 or self.faceDIR[3] == 1:
                            self.angle = 180
                            self.faceDIR = (0, 0, 1, 0)

                    if event.key == pygame.K_p:
                        Menu.isGamePaused = True

                    if event.key == pygame.K_RETURN and Menu.isGamePaused == True:
                        Menu.isGamePaused = False

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

        self.snakeHead = rot_img(sb.snakeHead, self.angle)
        self.snakeHead_rect = self.snakeHead.get_rect()

    def motion(self):
        if Menu.isGamePaused == False and Menu.gameRun == True:
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
            self.step = 0

    def throughWall(self):
        if self.xpos < -50:
            self.xpos = sb.xres
        if self.xpos > sb.xres + 50:
            self.xpos = -50
        if self.ypos > sb.yres:
            self.ypos = -50
        if self.ypos < -50:
            self.ypos = sb.yres



snakePlayer = snake()