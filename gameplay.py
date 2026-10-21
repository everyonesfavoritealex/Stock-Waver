"""
Author: Nicole and Alex
Date: 10-19-2026
Description:
"""
import pygame
from sys import exit
from spritesinit import Sprite_Object

def add_background_image():
    background_image = pygame.image.load( "assets/Background.PNG" )
    background_image = pygame.transform.scale( background_image, ( game_window_width, game_window_height ) )
    game_window.blit( background_image, ( 0, 0 ) )

def test_background():
    test_background = pygame.image.load( "assets/Test_Background.png" )
    test_background = pygame.transform.scale( test_background, ( game_window_width, game_window_height ) )
    game_window.blit( test_background, ( 0, 0 ) )

# Screen setup
pygame.init()

game_window_height = 894
game_window_width = 1280
game_window = pygame.display.set_mode( ( game_window_width, game_window_height ), pygame.RESIZABLE )

pygame.display.set_caption( "Stock Waver" )

clock = pygame.time.Clock()

gameplay_sprites = pygame.sprite.Group()
gameplay_sprites.add( Sprite_Object ( "assets/Newspaper.png", 300, 189, 820, 660 ) )
gameplay_sprites.add( Sprite_Object ( "assets/Phone.PNG", 102 , 325, -5, 185 ) )


# Starts game
game_running = True
while game_running == True:

    for event in pygame.event.get():

        # Allows player to x out
        if event.type == pygame.QUIT:
            game_running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
                exit()

    
    add_background_image()
    # test_background()
    gameplay_sprites.draw( game_window )
  
    pygame.display.update()
    clock.tick( 60 )