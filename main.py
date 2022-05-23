# Ilyès KHEROUA                              #PROJET TRANSVERSE
# Alicia LE BRUN                                  #SKY-FLY
# Maxime RIAD                                #christmas version


##########################################################################################################################################

# PROGRAMME PRINCIPAL

import pygame
from game import Game
from snowballs import Snowballs
from snowballs import Snowballs
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((626, 626))  # Taille de la fenêtre

# Définition du nom du jeu et mise en place du logo
pygame.display.set_caption("Sky-fly")  # Ecriture du nom du jeu sur la fenêtre
icon = pygame.image.load('images/logo.png').convert_alpha()
pygame.display.set_icon(screen)

# Importation de la bannière de démarrage
banner = pygame.image.load('images/banner.png')  # Chargement de l'image de la bannière
banner = pygame.transform.scale(banner, (300, 300))  # Reduction de la taille de l'image


# Chargement du jeu
game = Game()

running = True
down = False
timer = 250
cpt = 0
clock = pygame.time.Clock()
while running:
    clock.tick(timer)  # Vitesse de défilement & vitesse déplacement joueur
    # Si le jeu est en marche
    if game.is_playing:
        game.update(screen)
        game.score += 1
        cpt += 1
        if cpt == 1500:
            print("\nAttention, accélération !!")
            timer += 200
            cpt = 0

    # Sinon
    else:
        # Importation du fond d'écran d'accueil
        background = pygame.image.load('images/background.jpg')  # Chargement de l'image de fond
        screen.blit(background, (0, 0))

        screen.blit(banner, (157, 150))  # Mise en place de la bannière sur l'écran

        for i in range(0, 6):
            screen.blit(game.load_score.draw_score(i), game.load_score.score_rect)


        # Si aucun nom de joueur n'a été rentré
        if game.name_needed:
            game.enter_name(screen)

        pygame.display.flip()  # Mise à jour du jeu

    #Affichage d'une boule de neige



    # Pour chaque évènement du jeu :
    for event in pygame.event.get():

        # Si le joueur ferme la fenêtre :
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # Fermeture du jeu
            print("\nFermeture du jeu")  # Permet de nous informer personnellement du bon fonctionnement de la fermeture du jeu

        # Si le joueur touche le clavier :
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Si le joueur touche la touche "Entrée" :
            if event.key == pygame.K_RETURN:
                timer = 250
                game.start()  # Démarrage du jeu

        # Si le joueur lâche le clavier :
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            down = True

        #if game.pressed.get ( pygame.K_b):


    # Si le joueur presse la touche "Espace" et que le personnage est au dessus du sol :
    if game.pressed.get(pygame.K_SPACE) and game.player.rect.y > 0 :
         game.player.move_up() # Faire monter le joueur

    # Si le joueur lache le clavier et que le personnage est en dessous de la limite supérieure de la fenêtre :
    if down and game.player.rect.y <= 475:
        game.player.come_back_down() # Faire descendre le joueur