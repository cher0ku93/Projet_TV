import pygame
import random

class Snowball(pygame.sprite.Sprite):
    def __init__(self,snowball_event):
        super().__init__()
        self.image = pygame.image.load('images/snowball.png')
        self.image = pygame.transform.scale(self.image, (102, 102))
        self.rect = self.image.get_rect()
        self.velX = random.randint(1,5)
        self.velY = random.randint(1,3)
        self.rect.x = random.randint(300,900)
        self.rect.y = -random.randint(0,800)
        self.snowball_event = snowball_event
        '''
        self.v = 100
        self.alpha = 0
        self.alphaRadian = (3.14159 * (self.alpha /180))
        self. vv = self.v * math.sin(self.alphaRadian)
        self.vh = self.v * math.cos(self.alphaRadian)
        self.t = 0
        self.x = 0
        self.y = 0
        self.g = 9,81
        '''

    def remove(self):
        self.snowball_event.all_snowball.remove(self)

    def fall(self):
        self.rect.x -= self.velY
        self.rect.y +=self.velX

        # ne tombe pas sur le sol
        if self.rect.y >=500:
            print("Boule esquivée !")
            self.remove()
        #verifier si colision
        if self.snowball_event.game.check_collision(self, self.snowball_event.game.all_players):
            print("Père noël touché")
            self.remove()
            self.snowball_event.game.player.damage()


        '''
        if self.y >= 0:
            self.x = self.vh*self.t
            self.y = (self.vv * self.t) - self.g * self.t**2 /2
            self.t += 1
        '''








