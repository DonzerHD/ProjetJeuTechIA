import random


def affichage():
    pass

def attaquer(vie):
    pass


#fonction pour les fonctions
def les_potions():
    potions = random.randint(15, 50)
    nombre_potions = 3
    vie_joueur = 50
    if vie_joueur < 50 :
        if vie_joueur >= 1 and vie_joueur < 50 and nombre_potions >=1: 
           vie_joueur += random.randint(1, (50 -vie_joueur))
    else: print("il n'est pas nécessaire de prendre de potion")
    print("Vie maximum, vous pouvez maintenant attaquer !!!")
    return vie_joueur


def choix_du_joueur():
    pass

def verification_victoire_defaite(vie, partie_en_cours):
    pass





