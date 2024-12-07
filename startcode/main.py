import pygame
import sys

from startcode.breakout_module import *

venster_breedte = 590
venster_hoogte = 480
bal_positie = [290 , 240]
bal_grootte = 10
blok_breedte = 60
blok_hoogte = 20
blok_rijen = 5
blok_kolommen = venster_breedte // (blok_breedte + 5)
peddel_positie = [290 , venster_hoogte - 20]
peddel_breedte = 60
peddel_hoogte = 10
peddel_snelheid = 5
klok = pygame.time.Clock()
spel_voorbij = False

venster = setup_venster(venster_breedte, venster_hoogte)
bal_snelheid = initialiseer_bal()
blokken = initialiseer_blokken(blok_rijen, blok_kolommen, blok_breedte, blok_hoogte)

zwart = (0,0,0)
wit = (255, 255, 255)

def teken_spel():
    venster.fill(zwart)
    pygame.draw.rect(venster, wit, (peddel_positie[0] - (peddel_breedte // 2), peddel_positie[1], peddel_breedte, peddel_hoogte))
    pygame.draw.circle(venster, wit, bal_positie, bal_grootte)
    for blok in blokken:
        pygame.draw.rect(venster, wit, blok)
    pygame.display.update()

def beweeg_peddel():
    

while not spel_voorbij:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    teken_spel()
    bal_positie, bal_snelheid = update_bal()
    klok.tick(60)

