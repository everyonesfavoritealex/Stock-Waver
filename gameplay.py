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
delta=0
game_running = True
day_active=True
day=0
clicked=False
active_upgrades=[False,False,False,False,False,False]
max_stocks=False
stocks=utils.get_stocks(3)
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
    day+=1
    day_active=True
    active_upgrades=utils.get_active_upgrades(day)
    if active_upgrades[3] and not max_stocks:
        stocks.extend(utils.get_stocks(2))
    #TODO once upgrade sprites are added add code to add them to sprite group once day they're unlocked is reached
    if active_upgrades[2]:
        gameplay_sprites.add(Sprite_Object("assets/Newspaper.png", 300,189,820,660))
    if active_upgrades[4]:
        #coffee
        pass
    if active_upgrades[5]:
        #tv
        pass
    if active_upgrades[6]:
        #8ball
        pass
    if active_upgrades[7]:
        gameplay_sprites.add(Sprite_Object("assets/Phone.PNG",102,325,-5,185))
    while day_active:
        # Allows player to x out
        if event.type == pygame.QUIT:
            game_running = False
            exit()
        if event.type==pygame.MOUSEBUTTONUP:
            clicked=True

        delta = clock.tick(60) / 1000 # limits FPS to 60
        add_background_image()
        # test_background()
        gameplay_sprites.draw( game_window )
        
        pygame.display.update()
