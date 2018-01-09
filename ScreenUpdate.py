from Importer import *

def screenUpdate():
    clock = pygame.time.Clock()
    sb.gameDisplay.fill(sb.white)   # sets the background color.
    sb.gameDisplay.blit(opponent_1.oppoIMG, (opponent_1.oppoXpos, opponent_1.oppoYpos)) # shows the opponent.
    sb.gameDisplay.blit(snakePlayer.snakeHead, (snakePlayer.xpos, snakePlayer.ypos))    # shows the player.
    pygame.draw.circle(sb.gameDisplay, sb.green, (apple.appleXpos, apple.appleYpos), 5) # shows the apple.
    
    # text for the score.
    textoppoScore = "Oppo Score: " + str(opponent_1.oppoScore)
    textplayScore = "Your Score: " + str(snakePlayer.points)
    message_display(textoppoScore, sb.xres - 100, 50, 25, sb.gameDisplay)
    message_display(textplayScore, sb.xres - 100, 25, 25, sb.gameDisplay)
    
    clock.tick(60)      # frames per second of the game.
    pygame.display.update()
