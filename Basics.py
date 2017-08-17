import pygame

winningPoints = 10

xres = 800
yres = 600

snakeWidth = 50
snakeHeight = 50

white = (255, 255, 255)
green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((xres, yres))

background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image,(xres, yres))

snakeHead = pygame.image.load("Snake_head.png")
snakeHead = pygame.transform.scale(snakeHead, (snakeWidth, snakeHeight))