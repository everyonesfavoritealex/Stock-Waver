"""
Author: Nicole
Date: 10-19-2026
Description:
"""
import pygame
from spritesinit import Sprite
def add_background_image():
    background_image = pygame.image.load("assets/Background.PNG")
    background_image = pygame.transform.scale(background_image, ( game_window_height, game_window_width))
    gameplay_sprites.update()
    gameplay_sprites.draw(game_window)
    
    game_window.blit(background_image, (0, 0))
    game_window.blit(game_window,(0,0))
    pygame.display.update()



# Screen setup
pygame.init()
game_window_width = 894
game_window_height = 1280
phone=Sprite(100,700,"assets/Phone.PNG")
gameplay_sprites=pygame.sprite.Group()
gameplay_sprites.add(phone)

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