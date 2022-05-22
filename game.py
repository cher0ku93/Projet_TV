# PROGRAMME CONCERNANT LE JEU

import pygame
from player import Player
from sled import Sled
from tinsel import Tinsel
from score import Score
from inputbox import InputBox


# Création de la classe représentant le jeu
class Game:
    def __init__(self):

        # Concernant le jeu :
        self.is_playing = False # Le jeu n'est pas en marche
        self.pressed = {}
        # Importation du fond d'écran d'accueil
        self.background = pygame.image.load('images/background.jpg').convert()  # Chargement de l'image de fond
        self.x_background = 626

        # Concernant le joueur :
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)

        # Concernant les traineaux :
        self.all_sleds = pygame.sprite.Group()
        self.spawn_sled()

        # Concernant les guirlandes :
        self.all_tinsels = pygame.sprite.Group()
        self.spawn_tinsel()

        # Concernant le score :
        self.score = 0  # Initialisation du score
        self.load_score = Score()

        # Concernant l'input box :
        self.inputbox = InputBox(100, 100, 140, 32) # Création de l'instance de l'inputbox
        self.name_needed = False

        self.lifes_image = [pygame.image.load('images/hearts 1.png'), pygame.image.load('images/hearts 2.png'), pygame.image.load('images/hearts 3.png')]
        self.health_image = pygame.transform.scale(self.lifes_image[2], (120, 120))


    def test_score(self):
        self.load_score.new_score = self.score
        self.load_score.check_update()
        if self.load_score.name_needed:
            self.name_needed = True

    # Fonction qui permet d'entrer un pseudo dans l'inputbox
    def enter_name(self, screen):
        # Si l'inputbox n'a pas été créée :
        if not self.inputbox.done:
            for event in pygame.event.get():
                self.inputbox.handle_event(event)
            self.inputbox.update()
            self.inputbox.draw(screen) # Mise en place de l'inputbox sur l'écran

        # Sinon :
        else:
            self.load_score.name = self.inputbox.text
            self.name_needed = False
            self.load_score.update_score()


    # Début du jeu
    def start(self):
        self.is_playing = True # Le jeu est en marche
        self.paused = False # Le jeu n'est pas en pause
        print("\nLet's go ! :)")
        self.inputbox.done = False
        self.load_score.updated = False



    # Fin de jeu
    def game_over(self):
        print("\nScore :", self.score) # Affichage du score final
        self.is_playing = False # Le jeu n'est plus en marche
        self.all_sleds = pygame.sprite.Group()
        self.all_tinsels = pygame.sprite.Group()
        self.player.lives = self.player.max_lives  # Réinitialisation du nombre de vie à 3
        self.score = 0  # Réinitialisation du score à 0
        self.health_image = pygame.transform.scale(self.lifes_image[2], (120, 120))


    def update(self, screen):

        # Application de l'arrière plan & défilement en boucle
        mod = self.x_background % self.background.get_rect().width
        screen.blit(self.background, (mod - self.background.get_rect().width, 0))
        if mod < 626:
            screen.blit(self.background, (mod, 0))
        self.x_background -= 1
        screen.blit(self.player.image, self.player.rect) # Application de l'image du joueur

        self.all_sleds.draw(screen) # Affichage des traineaux
        self.all_tinsels.draw(screen)  # Affichage des guirlandes

        # Défilement des traineaux
        for sled in self.all_sleds:
            sled.scrolling()

        # Défilement des guirlandes
        for tinsel in self.all_tinsels:
            tinsel.scrolling()

        # Affichage du score
        font = pygame.font.SysFont('Verdana', 20, 0)  # Police d'écriture + taille + non gras
        score_text = font.render(f'Score : {self.score}', 1, (187, 255, 255)) # Mise en forme de l'affichage du score (police + couleur)
        screen.blit(score_text, (20, 20))  # Affichage sur écran

        screen.blit(self.health_image, (5, 20))
        pygame.display.flip()  # Mise à jour de l'écran

    # Fonction qui permet d'afficher les traineaux
    def spawn_sled(self):
        sled = Sled(self)
        self.all_sleds.add(sled)

    # Fonction qui permet d'afficher les guirlandes
    def spawn_tinsel(self):
        tinsel = Tinsel(self)
        self.all_tinsels.add(tinsel)

    # Fonction qui permet de détecter les collisions
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def handle_pause(self):
        for event in pygame.event.get():
            self.pause.check_pause(event)

    def update_health_image(self, life):
        if life <= 0:
            return
        self.health_image = pygame.transform.scale(self.lifes_image[life-1], (120, 120))






