

import pygame
import random
import math as math




class Snowballs(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.velocity = 5
        self.image = pygame.image.load('images/snowball.png')
        self.image = pygame.transform.scale ( self.image , (160 , 160) )
        self.rect = self.image.get_rect()
        k = 0  # frottement de l'air
        alpha = random.randint ( 0 , 180 ) * 2 * math.pi / 360
        m = 1
        g = 9.81
        v0 = 250 / 3.6
        vx0 = v0 * math.cos ( alpha )
        vy0 = v0 * math.sin ( alpha )
        dt = 0.05
        t = 0
        x = 0
        y = 0
        vx = vx0
        vy = vy0
        while y >= 0 :
            x = x + dt * vx
            y = y + dt * vy
            vx = vx + dt * vx * (-k / m)
            vy = vy + dt * vy * (-k / m) - dt * g
            t = t + dt
        self.rect.x = 300 + random.randint(400, 800) # Position du traineau sur l'axe des abscisses
        self.rect.y = -10  # Position du traineau sur l'axe des ordonnées
        self.velocityX = 600, x
        self.velocityY = -10,x

    def scrolling(self):
        # S'il y a une collision entre une guirlande et le joueur :
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage()
            self.remove() # Suppression de la guirlande touchée
            self.game.spawn_snowballs() # Apparition d'une nouvelle guirlande

        # Sinon
        else:
            self.rect.x -= self.velocity # Les guirlandes défilent

        if self.rect.x <= -160:
            self.rect.x = 600 + random.randint(300, 1000)  # Apparition d'une nouvelle guirlande

    # Fonction qui permet de supprimer les guirlandes
    def remove(self):
        self.game.all_tinsels.remove(self)




