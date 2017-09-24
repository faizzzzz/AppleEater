You compete with a computer to eat apples. Whoever eats 10 apples first, wins.

// Understanding the code //

1. Importer.py: imports classes from all files.
2. Launch.py: imports all the variables from Importer.py.
3. Basics.py: contains the basic vairables which are used by other .py files.
4. Snake.py: it is the snake class and inititates it with the variable snakePlayer.
5. Apple.py: it creates the apple class and keeps track of the player's score.
6. Opponent.py: creates the opponent class and keeps track of the opponent's score by importing apple.py.
7. Pause_Menu.py: creates the pause and menu screen.
8. Reset.py: it contains the reset function, which resets the game, and the gameEND function which determines the winner. The scores are then save to a text file.
9. Rotating_Image.py: contains a simple function to rotate an image from the center (instead of the top left coordinate).
10. ScreenUpdate.py: contains the screenUpdate function which imports all variable from Importer.py to blit the image on the gameDisplay. This allows for smooth movement of images.

For further explaination, read the comments in the code

// Info //
Use arrow keys to navigate. The player's speed is set to 5 whereas the computer's speed is 2.5. The player can go through walls and come through the other side whereas the computer can not.

HAVE FUN!!
