from Importer import *

if __name__ == "__main__":
    while True:
        if Menu.gameRun == False:
            Menu.menu()
        if Menu.gameRun == True:
            snakePlayer.motion()
            gameEnd()
            apple.score()
            opponent_1.oppoMove()
            snakePlayer.move()
            snakePlayer.throughWall()
            screenUpdate()