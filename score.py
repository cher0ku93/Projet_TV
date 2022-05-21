# PROGRAMME CONCERNANT LE SCORE

import pygame
import os
import json

# Création de la classe représentant le score
class Score:
    def __init__(self, score=0, username='test'):
        self.name_needed = False
        self.score_rect = (100, 400) # Coordonnées de l'affichage du score
        self.existing_files = False
        self.name = username
        self.new_score = score
        self.old_score = []
        self.check_files()
        self.load_old_scores()
        self.updated = False

    # Fonction qui permet l'affichage des meilleurs scores
    def draw_score(self, number):
        font1 = pygame.font.SysFont('Verdana', 20, 0) # Mise en forme de la police d'écriture de tous les scores
        font2 = pygame.font.SysFont('Verdana', 30, 1) # Mise en forme de la police d'écriture de "BEST SCORES"
        if number == 0:
            score_text = font2.render('BEST SCORES', 1, (3, 3, 3))
            self.score_rect = (20, 410) # Coordonnées de "BEST SCORES"
        else:
            score_text = font1.render(f"{number}: {self.old_score[number + number - 1]} pts for {self.old_score[number + number - 2]}", 1, (3, 3, 3))
            self.score_rect = (40, 450 + (28 * (number - 1))) # Coordonnées des scores
        return score_text

    # Fonction qui permet de détecter l'existence de 'score.txt'
    def check_files(self):
        # Si le fichier 'score.txt' existe :
        if os.path.exists('score.txt'):
            self.existing_files = True

        # Sinon
        else:
            self.creating_default() # Création d'un fichier 'score.txt' par defaut

    # Fonction qui permet la création d'un fichier 'score.txt'
    def creating_default(self):
        # Si le fichier n'existe pas encore :
        if not self.existing_files:
            default = open("score.txt", "w") # Ouverture d'un nouveau fichier 'score.txt' en mode écriture
            json.dump(["default", 5, "default", 4, "default", 3, "default", 2, "default", 1], default) # Remplissage du fichier avec cette ligne par défaut
            default.close() # Fermeture du fichier
            self.existing_files = True

    def load_old_scores(self):
        if self.existing_files:
            op = open("score.txt", "r") # Ouverture du fichier 'score.txt' en mode lecture
            self.old_score = json.load(op)
            op.close() # Fermeture du fichier

    def check_update(self):
        if self.new_score >= self.old_score[9]:
            self.name_needed = True

    def update_score(self):
        if not self.updated:
            file = open("score.txt", "w") # Ouverture du fichier 'score.txt' en mode écriture

            if self.new_score >= self.old_score[1]:
                for i in range(7, -1, -1):
                    self.old_score[i + 2] = self.old_score[i]
                self.old_score[0] = self.name
                self.old_score[1] = self.new_score

            elif self.new_score >= self.old_score[3]:
                for i in range(7, 1, -1):
                    self.old_score[i + 2] = self.old_score[i]
                self.old_score[2] = self.name
                self.old_score[3] = self.new_score

            elif self.new_score >= self.old_score[3]:
                for i in range(7, 3, -1):
                    self.old_score[i + 2] = self.old_score[i]
                self.old_score[4] = self.name
                self.old_score[5] = self.new_score

            elif self.new_score >= self.old_score[3]:
                for i in range(7, 5, -1):
                    self.old_score[i + 2] = self.old_score[i]
                self.old_score[6] = self.name
                self.old_score[7] = self.new_score

            elif self.new_score >= self.old_score[9]:
                self.old_score[8] = self.name
                self.old_score[9] = self.new_score

            json.dump(self.old_score, file)
            file.close() # Fermeture du fichier
            self.name_needed = False
            self.updated = True

