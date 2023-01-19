import unittest
import random
from utils import affichage , les_potions , attaquer

class TestJeux(unittest.TestCase):

    def test_attaquer(self):
        vie_joueur = 50
        
        vie_joueur = attaquer(vie_joueur)
        
        self.assertTrue(vie_joueur <= 100)  
        self.assertFalse(vie_joueur <= 0)
        
        vie_monstre = 100
        
        vie_monstre = attaquer(vie_monstre)
        
        self.assertTrue(vie_monstre <= 100)
        self.assertFalse(vie_monstre <= 0)
        
        vie_joueur = 50
        for i in range(100):
            vie_joueur = attaquer(vie_joueur)
            self.assertTrue(vie_joueur <= 100)
        
        vie_monstre = 100
        for i in range(100):
            vie_monstre = attaquer(vie_monstre)
            self.assertTrue(vie_monstre <= 100)

    def test_les_potions(self):
        random.seed(45)
        self.assertEqual(les_potions(45,50,3) ,(48,50,2))
        self.assertEqual(les_potions(12,50,2) ,(39,50,1))        
        self.assertEqual(les_potions(37,50,1) ,(45,50,0))
        
        
    def test_les_potions2(self):
        self.assertGreaterEqual(les_potions(45,50,3)[0],45)
        self.assertEqual(les_potions(12,50,2)[1],50)
        self.assertLessEqual(les_potions(37,50,1)[2],0)
          
    def test_verification_victoire_defaite(self):
        pass
    
    