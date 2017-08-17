import pygame, time
from Snake import snakePlayer
from Opponent import opponent_1
from Pause_Menu import Menu
import Basics as sb
from message import message_display

def reset():
    snakePlayer.points = 0
    opponent_1.oppoScore = 0
    snakePlayer.angle = 0
    snakePlayer.faceDIR = (1, 0, 0, 0)
    opponent_1.oppoXpos = 0
    opponent_1.oppoYpos = 0
    snakePlayer.xpos = sb.xres/2
    snakePlayer.ypos = sb.yres/2

winning_points = sb.winningPoints
def gameEnd():
    if snakePlayer.points == winning_points or opponent_1.oppoScore == winning_points:
        if snakePlayer.points == winning_points:
            message_display("You Win!!", sb.xres/2, sb.yres/2, 50, sb.gameDisplay)
        if opponent_1.oppoScore == winning_points:
            message_display("You Lost.", sb.xres/2, sb.yres/2, 50, sb.gameDisplay)
        pygame.display.update()
        time.sleep(2)
        reset()
        Menu.gameRun = False
        Menu.showMenu = True