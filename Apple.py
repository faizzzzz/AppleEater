import random
import Basics as sb
from Snake import snakePlayer

### Variables used in other files ###
# isAppleDrawn is used in Opponent.py.
# appleXpos is used in Opponent.py and ScreenUpdate.py.
# appleYpos is used in Opponent.py and ScreenUpdate.py.

class apple:
    def __init__(self):
        self.isAppleDrawn = False   # check to see if the apple is drawn or not.
        self.winningPoints = sb.winningPoints

    def score(self):
        if self.isAppleDrawn == False:
            # if the apple is not drawn, then draw the apple.
            self.appleXpos = random.randrange(25, sb.xres - 25)
            self.appleYpos = random.randrange(25, sb.yres - 25)

            self.isAppleDrawn = True

        if snakePlayer.xpos < self.appleXpos < snakePlayer.xpos + 50 and snakePlayer.ypos < self.appleYpos < snakePlayer.ypos + 50:
            # if the x and y position of the apple lies between the x position and width of the player and the y position and the height
            # of the player, then the player has eaten the apple/scored.
            ### the scoring method for the opponent is written in opponent.py file ###
            snakePlayer.points += snakePlayer.pointsINCR
            self.isAppleDrawn = False   # once the player eats the apple, the apple is no longer drawn in the same position.

apple = apple()
