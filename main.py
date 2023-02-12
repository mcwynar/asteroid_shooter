import pygame
import sys

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):

        # Init the parent class
        super().__init__(groups)

        # We need a surface -> image
        self.image = pygame.image.load('./graphics/ship.png').convert_alpha()

        # We need a rect
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        # timer
        self.can_shoot = True
        self.shoot_time = None

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True

    def input_position(self):
        position = pygame.mouse.get_pos()
        self.rect.center = position

    def laser_shoot(self):
        if pygame.mouse.get_pressed() == (1, 0, 0) and self.can_shoot:
            print('shoot laser')
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def update(self):
        self.laser_timer()
        self.laser_shoot()
        self.input_position()

class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)


# basic setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
clock = pygame.time.Clock()

# background
background_surf = pygame.image.load('./graphics/background.png').convert()

# sprite groups
spaceship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)
laser = Laser(laser_group, (200, 200))

# game loop
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick() / 1000

    # background
    display_surface.blit(background_surf, (0,0))

    # update
    spaceship_group.update()

    # graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)

    # draw the frame
    pygame.display.update()
