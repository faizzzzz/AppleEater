import random
import Basics as sb
from Snake import snakePlayer

class apple:
    def __init__(self):
        self.isAppleDrawn = False
        self.winningPoints = 10

    def score(self):
        if self.isAppleDrawn == False:
            self.appleXpos = random.randrange(25, sb.xres - 25)
            self.appleYpos = random.randrange(25, sb.yres - 25)

            self.isAppleDrawn = True

        if snakePlayer.xpos < self.appleXpos < snakePlayer.xpos + 50 and snakePlayer.ypos < self.appleYpos < snakePlayer.ypos + 50:
            snakePlayer.points += snakePlayer.pointsINCR
            self.isAppleDrawn = False

apple = apple()
# apple_2 = apple()