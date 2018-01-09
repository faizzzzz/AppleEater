import pygame
from Apple import apple
from Pause_Menu import Menu

class opponent:
    def __init__(self):
        self.oppoXpos = 0       # x position of the opponent.
        self.oppoYpos = 0       # y position of the opponent.
        self.oppoSpeedINCR = 2.5        # the speed of the opponent.(half the speed of the player).
        self.oppoScore = 0
        self.oppoEatApple = False       # to check if the opponent ate/collected the apple.
        self.textScoreOppo = "Oppo Score: " + str(self.oppoScore)
        self.oppoWidth = 50
        self.oppoHeight = 50

    def oppoMove(self):
        # loading the opponent image.
        self.oppoIMG = pygame.image.load("opponent.png")
        self.oppoIMG = pygame.transform.scale(self.oppoIMG, (self.oppoWidth, self.oppoHeight))
        self.oppoIMG_rect = self.oppoIMG.get_rect()
        if Menu.isGamePaused == False:
            self.oppoSpeed = self.oppoSpeedINCR     # the speed of the opponent.
            if self.oppoXpos + (self.oppoWidth/2) > apple.appleXpos:
                # if the x position of the opponent is greater than the x position of the apple, then the x position of the opponent is
                # decreased so that it moves closer to the apple.
                self.oppoXpos -= self.oppoSpeed
            if self.oppoXpos + (self.oppoWidth/2) < apple.appleXpos:
                # if the x position of the opponent is less then the x position of the apple, then the x position of the opponent is 
                # increased so that it moves closer to the apple.
                self.oppoXpos += self.oppoSpeed
            if self.oppoYpos + (self.oppoHeight/2) > apple.appleYpos:
                # if the y position of the opponent is greater than the y position of the apple(opponent is below the apple), then the 
                # y position of the opponent is decreased.
                self.oppoYpos -= self.oppoSpeed
            if self.oppoYpos + (self.oppoHeight/2) < apple.appleYpos:
                # if the y position of the opponent is less than the y position of the apple(opponent is aboe the apple), then the
                # y position of the apple is increased.
                self.oppoYpos += self.oppoSpeed
        if Menu.isGamePaused == True:
            # if the game is paused, the opponent does not move.
            self.oppoSpeed = 0


        if self.oppoXpos <= apple.appleXpos <= self.oppoXpos + self.self.oppoWidth and self.oppoYpos <= apple.appleYpos <= self.oppoYpos + self.self.oppoHeight:
            # if the x pos and y pos of the apple lie between the x position and and width and the y position and height of the 
            # opponent respectively, it means that the opponent has eaten the apple/scored.
            self.oppoScore += 1
            apple.isAppleDrawn = False

opponent_1 = opponent()
