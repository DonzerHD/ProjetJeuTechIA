import unittest
import random
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

    # def test_les_potions(self):
    #     random.seed(45)
    #     self.assertEqual(les_potions(45,50,3) ,(45,50,2))
    #     self.assertEqual(les_potions(12,50,2) ,(12,50,1))        
    #     self.assertEqual(les_potions(37,50,1) ,(37,50,0))
        
        
    def test_les_potions(self):
        self.assertGreaterEqual(les_potions(45,50,3)[0],45)
        self.assertEqual(les_potions(12,50,2)[1],50)
        self.assertLessEqual(les_potions(37,50,1)[2],0)
        
        
    
    
   
        
        
    def test_choix_du_joueur(self):
        pass
        # vie_joueur = 50
        # vie_monstre = 50
        # nombre_potions = 3
        # choix = 1
        # retour = choix_du_joueur(vie_joueur, vie_monstre, nombre_potions)
        # self.assertGreater(retour[0], vie_joueur)
        # self.assertLess(retour[1], vie_monstre)
        # self.assertEqual(retour[2], nombre_potions)
    
    def test_verification_victoire_defaite(self):
        pass
    
    