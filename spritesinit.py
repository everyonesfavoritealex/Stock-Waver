import pygame

class Sprite_Object( pygame.sprite.Sprite ):
    def __init__( self, image_path, scale_x, scale_y, topleft_x, topleft_y ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load( image_path )
        self.image = pygame.transform.scale( self.image, ( scale_x, scale_y ) )
        self.rect = self.image.get_rect( topleft = ( topleft_x, topleft_y ) )

    

# Background
def add_background_image(window, window_width, window_height):
    background_image = pygame.image.load( "assets/Background.PNG" )
    background_image = pygame.transform.scale( background_image, ( window_width, window_height ) )
    window.blit( background_image, ( 0, 0 ) )

# Title Background 
def title_background_image(window, window_width, window_height):
    background_image = pygame.image.load( "assets/Title_Background.png" )
    background_image = pygame.transform.scale( background_image, ( window_width, window_height ) )
    window.blit( background_image, ( 0, 0 ) )

# Testing Background
def test_background(window, window_width, window_height):
    test_background = pygame.image.load( "assets/Test_Background.png" )
    test_background = pygame.transform.scale( test_background, ( window_width, window_height ) )
    window.blit( test_background, ( 0, 0 ) )
