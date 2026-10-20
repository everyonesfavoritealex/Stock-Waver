"""
Author: Nicole
Date: 10-19-2026
Description:
"""
import pygame

def add_background_image():
    background_image = pygame.image.load("assets/Background.PNG")
    background_image = pygame.transform.scale(background_image, ( game_window_height, game_window_width))
    game_window.blit(background_image, (0, 0))
    pygame.display.update()



# Screen setup
pygame.init()
game_window_width = 894
game_window_height = 1280
game_window = pygame.display.set_mode((game_window_height, game_window_width))
game_running = True

# Starts game
while game_running == True:

    for event in pygame.event.get():

        # Allows player to x out
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False

    add_background_image()