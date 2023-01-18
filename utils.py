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
    choix = int(input("Entrez 1 pour attaquer ou 2 pour prendre une potion de vie : "))
    tour_fini= False
    while not tour_fini:
        if choix == 1:
            tour_fini = True
            attaquer()
        elif choix == 2:
            tour_fini = True
            les_potions()
        else:
            choix = int(input("Erreur, entrez à nouveau votre choix, 1 pour attaquer ou 2 pour prendre la potion de soin :"))
def verification_vitoire_defaite(vie, partie_en_cours):
     if vie_joueur <= 0:
         print("Le Monstre a gg")
     elif vie_monstre <= 0:
         print("Le Joueur a gg")
     partie_en_cours = False
