import pygame

class Sprite_Object( pygame.sprite.Sprite ):
    def __init__( self, image_path, scale_x, scale_y, topleft_x, topleft_y ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load( image_path )
        self.image = pygame.transform.scale( self.image, ( scale_x, scale_y ) )
        self.rect = self.image.get_rect( topleft = ( topleft_x, topleft_y ) )

    
# Background
def add_background(window, window_width, window_height, file_name):
    add_background = pygame.image.load( f"assets/{file_name}" )
    add_background = pygame.transform.scale( add_background, ( window_width, window_height ) )
    window.blit( add_background, ( 0, 0 ) )