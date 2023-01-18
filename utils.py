import random

def affichage(vie_joueur, vie_monstre , nombre_potions):
    print("="*20)
    print("Joueur :",vie_joueur," PV | Monstre :",vie_monstre," PV | Potions :",nombre_potions)
    print("="*20)

def attaquer(vie_joueur, vie_monstre):
    degat = random.randint(0, 10)
    if degat > 7:
        print("coup critique")
    elif degat < 7 and degat > 0:
        print("coup normal")
    elif degat == 0:
        print("Esquive")
    vie_monstre = vie_monstre- degat 
    return vie_joueur , vie_monstre
    


def les_potions(vie_joueur, vie_monstre, nombre_potions):
    if vie_joueur == 50:
        print("Il n'est pas necessaire de prendre une potion")
        choix_du_joueur(vie_joueur, vie_monstre, nombre_potions)
    elif nombre_potions == 0:
            print("Toutes les potions sont utilisées")
            choix_du_joueur(vie_joueur, vie_monstre , nombre_potions)
    elif vie_joueur < 50 :
           nombre_potions -= 1
           vie_joueur += random.randint(1, (50 - vie_joueur))
    return vie_joueur , vie_monstre , nombre_potions

def choix_du_joueur(vie_joueur, vie_monstre, nombre_potions):
    choix = int(input("Entrez 1 pour attaquer ou 2 pour prendre une potion de vie : "))
    tour_fini= False
    while not tour_fini:
        if choix == 1:
            tour_fini = True
            vie_joueur, vie_monstre = attaquer(vie_joueur, vie_monstre)
            return vie_joueur, vie_monstre , nombre_potions
        elif choix == 2:
            tour_fini = True
            vie_joueur, vie_monstre , nombre_potions = les_potions(vie_joueur, vie_monstre, nombre_potions)
            return vie_joueur, vie_monstre , nombre_potions
        else:
            choix = int(input("Erreur, entrez à nouveau votre choix, 1 pour attaquer ou 2 pour prendre la potion de soin :"))

def verification_vitoire_defaite(vie_joueur, vie_monstre):
    if vie_joueur <= 0:
        print("Le Monstre a gg")
        return False
    elif vie_monstre <= 0:
        print("Le Joueur a gg")
        return False
    return True