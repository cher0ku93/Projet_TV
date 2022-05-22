# PROGRAMME CONCERNANT LES TRAINEAUX EN FEU

import pygame
import random

# Création de la classe représentant les traineaux
class Sled(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('images/sled.gif')  # Chargement de l'image d'un traineau
        self.image = pygame.transform.scale(self.image, (160, 160))  # Réduction de la taille de l'image du traineau
        self.rect = self.image.get_rect()
        self.rect.x = 600 + random.randint(400, 1000)  # Position du traineau sur l'axe des abscisses
        self.rect.y = 450  # Position du traineau sur l'axe des ordonnées
        self.velocity = 1  # Vitesse de défilement du traineau

    # Fonction qui permet aux traineaux de défiler
    def scrolling(self):
        # S'il y a une collision entre un traineau et le joueur :
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage()
            self.remove() # Suppression du traineau touché
            self.game.spawn_sled() # Apparition d'un nouveau traineau
        # Sinon
        else:
            self.rect.x -= self.velocity # Les traineaux défilent

        if self.rect.x <= -160:
            self.rect.x = 600 + random.randint(300, 1000)  # Apparition d'un nouveau traîneau


    # Fonction qui permet de supprimer les traineaux
    def remove(self):
        self.game.all_sleds.remove(self)