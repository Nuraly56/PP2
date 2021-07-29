import pygame
import random
 
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, WIDTH, HEIGHT):
        super().__init__()
        
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, WIDTH)
 
    def update(self):
        self.rect.y += 1
        
        if self.rect.y > 410:
            self.reset_pos()
 
 
class Player(Block):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class GreenBlock(Block):
    def update(self):
        self.rect.y -= 1
        if self.rect.y < -10:
            self.reset_pos()
 

pygame.init()
 
WIDTH = 700
HEIGHT = 400

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Hungry_Lion")

block_list_1 = pygame.sprite.Group()
block_list_2 = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    block_1 = GreenBlock(GREEN, 20, 15)

    block_1.rect.x = random.randrange(WIDTH)
    block_1.rect.y = random.randrange(HEIGHT)
 
    block_list_1.add(block_1)
    all_sprites_list.add(block_1)

    
    block_2 = Block(RED, 20, 15)

    block_2.rect.x = random.randrange(WIDTH)
    block_2.rect.y = random.randrange(HEIGHT)
 
    block_list_2.add(block_2)
    all_sprites_list.add(block_2)
 
lion = Player(BLUE, 20, 15)
all_sprites_list.add(lion)
 
done = False

font_score = pygame.font.SysFont("None", 50)
 
clock = pygame.time.Clock()
 
score = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(WHITE)
 
    all_sprites_list.update()
 
    blocks_hit_list_1 = pygame.sprite.spritecollide(lion, block_list_1, False)
    blocks_hit_list_2 = pygame.sprite.spritecollide(lion, block_list_2, False)
 
    for block_1 in blocks_hit_list_1:
        score += 1
        block_1.reset_pos()
    
    for block_2 in blocks_hit_list_2:
        score -= 1
        block_2.reset_pos()
 
    all_sprites_list.draw(screen)

    value = font_score.render("Score: " + str(score), True, YELLOW)
    screen.blit(value, [10, 10])
 
    clock.tick(20)

    pygame.display.flip()
 
pygame.quit()