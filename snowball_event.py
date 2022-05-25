import pygame
from snowball import Snowball

class SnowBallEvent:
    # création d'un compteur d'evenement
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 30
        self.game = game

        #Sprite pour un groupe de boule de neige
        self.all_snowball = pygame.sprite.Group()


    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loaded(self):
        return self.percent >=100

    def reset_percent(self):
        self.percent = 0

    def snow_fall(self):
        self.all_snowball.add(Snowball(self))


    def attempt_fall(self):
        #jauge totalement chargé
        if self.is_full_loaded():
            print("BOULE DE NEIGE !!!")
            self.snow_fall()
            self.reset_percent()



    def update_bar(self, surface):

        #ajout pourcentage
        self.add_percent()

        #declenchement de la tempête de boule de neige
        self.attempt_fall()

        #barre noir (arrière plan)
        pygame.draw.rect(surface, (0,0,0),[
            0, #axe x
            surface.get_height()-20, #axe des y
            surface.get_width(),# longueur de la fenêtre
            10# epaisseur barre

        ])
        #barre rouge (event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe x
            surface.get_height() - 20,
            (surface.get_width() / 100) * self.percent,
            10  # epaisseur barre
            ])




