import pygame
from Apple import apple
from Pause_Menu import Menu

class opponent:
    def __init__(self):
        self.oppoXpos = 0
        self.oppoYpos = 0
        self.oppoSpeedINCR = 2.5
        self.oppoScore = 0
        self.oppoEatApple = False
        self.textScoreOppo = "Oppo Score: " + str(self.oppoScore)

    def oppoMove(self):
        self.oppoIMG = pygame.image.load("opponent.png")
        self.oppoIMG = pygame.transform.scale(self.oppoIMG, (50, 50))
        self.oppoIMG_rect = self.oppoIMG.get_rect()
        if Menu.isGamePaused == False:
            self.oppoSpeed = self.oppoSpeedINCR
            if self.oppoXpos + 25 > apple.appleXpos:
                self.oppoXpos -= self.oppoSpeed
            if self.oppoXpos + 25 < apple.appleXpos:
                self.oppoXpos += self.oppoSpeed
            if self.oppoYpos + 25 > apple.appleYpos:
                self.oppoYpos -= self.oppoSpeed
            if self.oppoYpos + 25 < apple.appleYpos:
                self.oppoYpos += self.oppoSpeed
        if Menu.isGamePaused == True:
            self.oppoSpeed = 0


        if self.oppoXpos <= apple.appleXpos <= self.oppoXpos + 50 and self.oppoYpos <= apple.appleYpos <= self.oppoYpos + 50:
            self.oppoScore += 1
            apple.isAppleDrawn = False

opponent_1 = opponent()