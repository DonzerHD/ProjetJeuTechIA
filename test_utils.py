import unittest
from utils import affichage , les_potions , choix_du_joueur , attaquer , verification_vitoire_defaite

class TestJeux(unittest.TestCase):

    def test_attaquer(self):
        vie_joueur = 50
        vie_monstre = 100
        
        vie_joueur, vie_monstre = attaquer(vie_joueur, vie_monstre)
        
        self.assertTrue(vie_monstre <= 100)  
        self.assertFalse(vie_monstre <= 0)
        self.assertEqual(vie_joueur, 50)
        
        vie_joueur = 50
        vie_monstre = 100
        
        vie_monstre, vie_joueur= attaquer(vie_monstre, vie_joueur)
        
        self.assertTrue(vie_joueur <= 50)
        self.assertFalse(vie_joueur <= 0)
        self.assertEqual(vie_monstre, 100)
        
        vie_joueur = 50
        vie_monstre = 100
        for i in range(100):
            vie_joueur, vie_monstre = attaquer(vie_joueur, vie_monstre)
            self.assertTrue(vie_monstre <= 100)
        
        vie_joueur = 50
        vie_monstre = 100
        for i in range(100):
            vie_monstre, vie_joueur = attaquer(vie_monstre, vie_joueur)
            self.assertTrue(vie_joueur <= 50)

    def test_les_potions(self):
        pass
    
    def test_choix_du_joueur(self):
        pass
    
    def test_verification_victoire_defaite(self):
        pass