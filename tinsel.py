# PROGRAMME CONCERNANT LES GUIRLANDES MALEFIQUES

import pygame
import random

# Création de la classe représentant les guirlandes
class Tinsel(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('images/tinsel.png')  # Chargement de l'image d'une guirlande
        self.image = pygame.transform.scale(self.image, (150, 300))  # Réduction de la taille de l'image de la guirlande
        self.rect = self.image.get_rect()
        self.rect.x = 300 + random.randint(400, 800)  # Position de la guirlande sur l'axe des abscisses
        self.rect.y = -10  # Position de la guirlande sur l'axe des ordonnées
        self.velocity = 1  # Vitesse de défilement de la guirlande


    # Fonction qui permet aux guirlandes de défiler
    def scrolling(self):
        # S'il y a une collision entre une guirlande et le joueur :
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage()
            self.remove() # Suppression de la guirlande touchée
            self.game.spawn_tinsel() # Apparition d'une nouvelle guirlande

        # Sinon
        else:
            self.rect.x -= self.velocity # Les guirlandes défilent

        if self.rect.x <= -160:
            self.rect.x = 600 + random.randint(300, 1000)  # Apparition d'une nouvelle guirlande

    # Fonction qui permet de supprimer les guirlandes
    def remove(self):
        self.game.all_tinsels.remove(self)