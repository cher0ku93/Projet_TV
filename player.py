# PROGRAMME CONCERNANT LE JOUEUR

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('images/player.png') # Chargement de l'image du joueur
        #self.image = pygame.transform.scale(self.image, (102, 102))  # Reduction de la taille de l'image du personnage
        self.rect = self.image.get_rect()
        self.rect.x = 20  # Position du joueur sur l'axe des abscisses
        self.rect.y = 475  # Position du joueur sur l'axe des ordonnées
        self.velocity1 = 13 # Vitesse du joueur
        self.velocity2 = 9
        self.lives = 3  # Nombre de vie du joueur
        self.max_lives = 3  # Nombre maximal de vie que le joueur peut avoir

    # Fonction qui permet de faire monter le joueur
    def move_up(self):
        self.rect.y -= self.velocity1

    # Fonction qui permet de faire redescendre le joueur
    def come_back_down(self):
        self.rect.y += self.velocity2

    # Fonction concernant les dégâts faits au joueur
    def damage(self):
        self.lives -= 1 # Le nombre de vies du joueur diminue de 1
        # Si le joueur a maximum 0 vie :
        if self.lives <= 0:
            self.game.test_score()
            self.game.game_over()
            print("\nGame over :(")  # Annonce la fin de la partie

