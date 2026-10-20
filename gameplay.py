"""
Author: Nicole
Date: 10-19-2026
Description:
"""
import pygame
from sys import exit
from spritesinit import Sprite

class Newpaper_Object(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load( "assets/Newspaper.png" )
        self.image = pygame.transform.scale( self.image, ( 300, 189 ) )
        self.rect = self.image.get_rect( topleft = ( 820, 660 ) )

class Phone_Object(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load( "assets/Phone.PNG" )
        self.image = pygame.transform.scale( self.image, ( 102, 325 ) )
        self.rect = self.image.get_rect( topleft = ( -5, 185 ) )

def add_background_image():
    background_image = pygame.image.load( "assets/Background.PNG" )
    background_image = pygame.transform.scale( background_image, ( game_window_width, game_window_height ) )
    game_window.blit( background_image, ( 0, 0 ) )

def test_background():
    test_background = pygame.image.load( "assets/Test_Background.png" )
    test_background = pygame.transform.scale( test_background, ( game_window_width, game_window_height ) )
    game_window.blit( test_background, ( 0, 0 ) )

# Alex's Test Stuff
def add_background_image():
    background_image = pygame.image.load("assets/Background.PNG")
    background_image = pygame.transform.scale(background_image, ( game_window_width, game_window_height))
    gameplay_sprites.update()
    gameplay_sprites.draw(game_window)
    
    game_window.blit(background_image, (0, 0))
    game_window.blit(game_window,(0,0))
    pygame.display.update()


# Screen setup
pygame.init()

game_window_height = 894
game_window_width = 1280
game_window = pygame.display.set_mode( ( game_window_width, game_window_height ), pygame.RESIZABLE )

# Alex's Test Stuff
phone=Sprite(100,700,"assets/Phone.PNG")
gameplay_sprites=pygame.sprite.Group()
gameplay_sprites.add(phone)

pygame.display.set_caption( "Stock-Waver" )

clock = pygame.time.Clock()

newpaper = pygame.sprite.GroupSingle()
newpaper.add(Newpaper_Object())

phone = pygame.sprite.GroupSingle()
phone.add(Phone_Object())

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
    newpaper.draw( game_window )
    phone.draw( game_window )
    pygame.display.update()
    clock.tick( 60 )