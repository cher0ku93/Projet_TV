# PROGRAMME CONCERNANT LES INPUTBOX

import pygame

# Création de la classe représentant les inputbox
class InputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, text='ENTER A NAME'):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        self.inactive_color = pygame.Color('red1') # Couleur initiale de l'inputbox (rouge)
        self.active_color = pygame.Color('white') # Couleur de l'inputbox lorsqu'on clique dessus (blanc)
        self.color = self.inactive_color # Initialisation de la couleur au statut "inactif" (rouge)
        self.text = text
        self.font = pygame.font.SysFont('Verdana', 18, 0) # Mise en forme de la police d'écriture dans l'inputbox
        self.text_surface = self.font.render(text, True, self.color)
        self.active = False
        self.done = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.text = ""
            else:
                self.active = False
            self.color = self.active_color if self.active else self.inactive_color

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_w :
                    print(self.text)
                    self.done = True

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    self.text += event.unicode

                self.text_surface = self.font.render(self.text, True, self.color)

    def update(self):
        width = max(180, self.text_surface.get_width() + 10)
        self.rect.w = width

    # Fonction permettant la mise en forme de l'inputbox
    def draw(self, screen):
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5)) # Mise en place de la box sur l'écran de jeu
        pygame.draw.rect(screen, self.color, self.rect, 2)