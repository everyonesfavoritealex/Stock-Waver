import pygame
from spritesinit import Sprite_Object, add_background

# Screen setup
pygame.init()
pygame.font.init()

game_window_height = 894
game_window_width = 1280
game_window = pygame.display.set_mode( ( game_window_width, game_window_height ), pygame.RESIZABLE )

pygame.display.set_caption( "Stock Waver" )

clock = pygame.time.Clock()

play_button_sprite = pygame.sprite.Group()

play_button_sprite.add( Sprite_Object ( "assets/Title_Play_Button.png", 800, 129, game_window_width / 5, game_window_height / 2 ) )

pygame.font.Font( "fonts/Stock_waver-Regular.ttf", )

delta = 0
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
    
        delta = clock.tick(60) / 1000 # limits FPS to 60

        add_background( game_window, game_window_width, game_window_height, "Title_Background.png" )
        play_button_sprite.draw( game_window )

        pygame.display.update()
