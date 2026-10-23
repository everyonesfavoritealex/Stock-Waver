"""
Author: Nicole and Alex
Date: 10-19-2026
Description:
"""
import pygame
from sys import exit
from spritesinit import Sprite_Object, add_background
from utils import get_active_upgrades as gau, stocks

# Screen setup
pygame.init()

game_window_height = 894
game_window_width = 1280
game_window = pygame.display.set_mode( ( game_window_width, game_window_height ), pygame.RESIZABLE )

pygame.display.set_caption( "Stock Waver" )

clock = pygame.time.Clock()

gameplay_sprites = pygame.sprite.Group()
clock_sprite = pygame.sprite.Group()
pc_sprite = pygame.sprite.Group()

clock_sprite.add( Sprite_Object ( "assets/Clock_Base_Red.png", 190, 192, 1075, 100 ) )
clock_sprite.add( Sprite_Object ( "assets/Clock_Base_White.png", 190, 192, 1075, 100 ) )
clock_sprite.add( Sprite_Object ( "assets/Clock_Hands.png", 190, 192, 1075, 98 ) )
clock_sprite.add( Sprite_Object ( "assets/Clock_Hashs.png", 190, 192, 1075, 100 ) )

pc_sprite.add( Sprite_Object ( "assets/PC_Body.png", 955, 799, 155, 50 ) )

# Testing Sprites 
# gameplay_sprites.add( Sprite_Object ( "assets/Newspaper.png", 300, 189, 820, 660 ) ) # Newspapers
# gameplay_sprites.add( Sprite_Object ( "assets/Phone.PNG", 100 , 319, -5, 185 ) ) # Phone
# gameplay_sprites.add( Sprite_Object ( "assets/Magic_8_Ball.PNG", 90, 94, 370, 660) ) # Magic 8 Ball
# gameplay_sprites.add( Sprite_Object ( "assets/TV_Blank_Screen.png", 370, 406, 8, 440 ) ) # TV Blank
# gameplay_sprites.add( Sprite_Object ( "assets/TV_Breaking_News.png", 370, 406, 8, 440 ) ) # TV Breaking News
# gameplay_sprites.add( Sprite_Object ( "assets/TV_Blank_Cover.png", 370, 406, 8, 440 ) ) # TV Cover
# gameplay_sprites.add( Sprite_Object ( "assets/Cup_With_Coffee.png", 160, 322, 1110, 495 ) ) # Coffee
# gameplay_sprites.add( Sprite_Object ( "assets/Cup_Empty.png", 160, 322, 1110, 495 ) ) # Empty Cup
# gameplay_sprites.add( Sprite_Object ( "assets/Coffee_Top.png", 160, 322, 1110, 495 ) ) # Coffee Top

# Starts game
delta = 0
game_running = True
day_active = True
day = 0
clicked = False
active_upgrades = [ False, False, False, False, False, False ]
max_stocks = False
stocks = stocks.get_stocks(3)

while game_running == True:

    for event in pygame.event.get():
        # Allows player to x out
        if event.type == pygame.QUIT:
            game_running = False
            exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE:
        #         game_running = False
        #         exit()
    
    day += 1
    day_active = True

    active_upgrades = gau.get_active_upgrades( day )

    # Stocks Upgrade
    if active_upgrades[3] and not max_stocks:
        stocks.extend( stocks.get_stocks(2) )

    # Newspaper Upgrade
    if active_upgrades[2]:
        gameplay_sprites.add( Sprite_Object( "assets/Newspaper.png", 300, 189, 820, 660 ) )

    # Coffee Upgrade
    if active_upgrades[4]:
        gameplay_sprites.add( Sprite_Object ( "assets/Cup_Empty.png", 160, 322, 1110, 495 ) )
        pass

    # Breaking News Upgrade
    if active_upgrades[5]:
        gameplay_sprites.add( Sprite_Object ( "assets/TV_Breaking_News.png", 370, 406, 8, 440 ) )
        pass

    # Magic 8 Ball Upgrade
    if active_upgrades[6]:
        gameplay_sprites.add( Sprite_Object ( "assets/Magic_8_Ball.PNG", 90, 94, 370, 660) )
        pass

    # Insider Trading Upgrade
    if active_upgrades[7]:
        gameplay_sprites.add( Sprite_Object ( "assets/Phone.PNG", 100, 319, -5, 185 ) )

    
    while day_active:
        
        for event in pygame.event.get():
            # Allows player to x out
            if event.type == pygame.QUIT:
                game_running = False
                exit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = True

        delta = clock.tick(60) / 1000 # limits FPS to 60

        add_background( game_window, game_window_width, game_window_height, "Background.PNG" )
        # add_background( game_window, game_window_width, game_window_height, "Test_Background.png" )
        pc_sprite.draw( game_window )
        clock_sprite.draw( game_window )
        gameplay_sprites.draw( game_window )

        pygame.display.update()
