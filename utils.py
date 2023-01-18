import random

vie_joueur = 50

def affichage():
    pass

def attaquer(vie):
    degat = random.randint(0, 10)
    if degat > 7:
        print("coup critique")
    elif degat < 7 and degat > 0:
        print("coup normal")
    elif degat == 0:
        print("Esquive")
    vie = vie - degat 
    return vie
    

def les_potions():
    pass

def choix_du_joueur():
    pass

def verification_vitoire_defaite(vie, partie_en_cours):
     if vie_joueur <= 0:
         print("Le Monstre a gg")
     elif vie_monstre <= 0:
         print("Le Joueur a gg")
     partie_en_cours = False
