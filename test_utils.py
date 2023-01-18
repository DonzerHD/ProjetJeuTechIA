import unittest
from utils import affichage , les_potions , choix_du_joueur , attaquer , verification_vitoire_defaite

class TestJeux(unittest.TestCase):

    def test_attaquer(self):
        vie_joueur = 100
        vie_monstre = 50

        vie_joueur, vie_monstre = attaquer(vie_joueur, vie_monstre)
        self.assertLess(vie_monstre, 50)

    def test_les_potions(self):
        pass
    
    def test_choix_du_joueur(self):
        pass
    
    def test_verification_victoire_defaite(self):
        pass