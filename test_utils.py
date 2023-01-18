import unittest
from utils import affichage , les_potions , choix_du_joueur , attaquer , verification_vitoire_defaite

class TestJeux(unittest.TestCase):

    def test_attaquer(self):
        pass

    def test_les_potions(self):
        self.assertGreater(les_potions(45,50,3) ,(45,50,2))
        self.assertGreater(les_potions(12,50,2) ,(12,50,1))
        self.assertGreater(les_potions(37,50,1) ,(37,50,0))
        
        
    def test_choix_du_joueur(self):
        pass
    
    def test_verification_victoire_defaite(self):
        pass