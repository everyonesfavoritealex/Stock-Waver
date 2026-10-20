import pygame
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image_file):
        # 1. Initialize the parent Sprite class
        super().__init__()
        
        # 2. Define the image
        self.image = pygame.Surface((50, 50))
        
    
        self.image=pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (100, 100))
        # 3. Sprite rectangle for positioning and hitbox
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)