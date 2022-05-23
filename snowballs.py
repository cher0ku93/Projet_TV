

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
        self.rect.x = 300 + random.randint(400, 800) # Position du traineau sur l'axe des abscisses
        self.rect.y = -10  # Position du traineau sur l'axe des ordonnées
        self.velocityX = 100
        self.velocityY = -10

    def scrolling(self):
        # S'il y a une collision entre une guirlande et le joueur :
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage()
            self.remove() # Suppression de la guirlande touchée
            self.game.spawn_snowballs() # Apparition d'une nouvelle guirlande

        # Sinon
        else:
            self.rect.x -= self.velocityY # Les guirlandes défilent
            self.rect.y = self.velocityX


        if self.rect.x <= -160:
            self.rect.x = 600 + random.randint(300, 1000)  # Apparition d'une nouvelle guirlande

    # Fonction qui permet de supprimer les guirlandes
    def remove(self):
        self.game.all_tinsels.remove(self)




