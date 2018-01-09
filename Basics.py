import pygame

winningPoints = 10    # The number apples that need to be collected in order to win.

xres = 800
yres = 600

snakeWidth = 50
snakeHeight = 50

white = (255, 255, 255)
green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((xres, yres))

# background_image = pygame.image.load("background.jpg")
# background_image = pygame.transform.scale(background_image,(xres, yres))

# loading the image.
snakeHead = pygame.image.load("Snake_head.png")
snakeHead = pygame.transform.scale(snakeHead, (snakeWidth, snakeHeight))
