import random


def score(nombre_victoire, vie_monstre):
    if vie_monstre <= 0: 
        nombre_victoire += 1
    return nombre_victoire
    
def affichage(vie_joueur, vie_monstre , nombre_potions , joueur_nom, monstre_nom, nombre_victoire):
    """
    La fonction affichage() affiche l'état actuel du joueur, du monstre et du nombre de potions disponibles.

    Args:
    vie_joueur (int): la vie actuelle du joueur
    vie_monstre (int): la vie actuelle du monstre
    nombre_potions (int): le nombre de potions disponibles pour le joueur
    """   
    print("="*20)
    print("Héros[",joueur_nom,"] :",vie_joueur," PV | Méchants[",monstre_nom,"] :" , vie_monstre ," PV | Potions :",nombre_potions , " Score :", nombre_victoire)
    print("="*20)

def attaquer(vie_personne_attaquee):
    """
    La fonction attaquer() simule une attaque contre une personne. Elle génère aléatoirement des dégâts infligés par l'attaque et affiche un message en conséquence.
    Args:
    vie_personne_attaquee (int): la vie actuelle de la personne qui subit l'attaque.
    Returns:
    int : la vie mise à jour de la personne après l'attaque.
    """
    degat = random.randint(0, 10)
    if degat > 7:
        print("coup critique")
    elif degat < 7 and degat > 0:
        print("coup normal")
    elif degat == 0:
        print("Esquive")
    vie_personne_attaquee = vie_personne_attaquee - degat 
    return vie_personne_attaquee
    


def les_potions(vie_joueur, vie_monstre, nombre_potions):
    """
    La fonction les_potions() gère l'utilisation des potions par le joueur dans un jeu. Elle vérifie si le joueur a besoin d'utiliser une potion, si des potions sont disponibles, et si oui, utilise une potion pour augmenter la vie du joueur.

    Args:
    vie_joueur (int): la vie actuelle du joueur
    vie_monstre (int): la vie actuelle du monstre
    nombre_potions (int): le nombre de potions disponibles pour le joueur

    Returns:
    tuple: un tuple contenant la vie mise à jour du joueur, de la vie du monstre et du nombre de potions restantes après utilisation de la potion.
    (vie_joueur, vie_monstre, nombre_potions)
    """
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
    """
    La fonction choix_du_joueur() permet au joueur de faire un choix entre attaquer ou utiliser une potion. Elle vérifie si le choix est valide et appelle la fonction appropriée en conséquence.

    Args:
    vie_joueur (int): la vie actuelle du joueur
    vie_monstre (int): la vie actuelle du monstre
    nombre_potions (int): le nombre de potions disponibles pour le joueur

    Returns:
    tuple: un tuple contenant la vie mise à jour du joueur, de la vie du monstre et du nombre de potions restantes après le choix du joueur.
    (vie_joueur, vie_monstre, nombre_potions)
    """
    choix = int(input("Entrez 1 pour attaquer ou 2 pour prendre une potion de vie : "))
    tour_fini= False
    while not tour_fini:
        if choix == 1:
            tour_fini = True
            vie_monstre = attaquer(vie_monstre)
            return vie_joueur, vie_monstre , nombre_potions
        elif choix == 2:
            tour_fini = True
            vie_joueur, vie_monstre , nombre_potions = les_potions(vie_joueur, vie_monstre, nombre_potions)
            return vie_joueur, vie_monstre , nombre_potions
        else:
            choix = int(input("Erreur, entrez à nouveau votre choix, 1 pour attaquer ou 2 pour prendre la potion de soin :"))

def verification_victoire_defaite(vie_joueur, vie_monstre, nombre_potions, monstre , adversaire):
    """
    La fonction verification_victoire_defaite() vérifie si le jeu est terminé en raison d'une victoire ou d'une défaite d'un des joueurs.

    Args:
    vie_joueur (int): la vie actuelle du joueur
    vie_monstre (int): la vie actuelle du monstre
    nombre_potions (int): le nombre de potions disponibles pour le joueur
    monstre (list): liste des monstres
    adversaire (str): nom de monstre actuel

    Returns:
    tuple: un tuple contenant un booléen indiquant si le jeu est terminé (False) ou pas (True), la vie mise à jour du joueur, de la vie du monstre, du nombre de potions restantes et du nom du monstre suivant
    (bool, vie_joueur, vie_monstre, nombre_potions, adversaire)
    """
    if vie_joueur <= 0:
        print("Perdu")
        return False , vie_joueur , vie_monstre , nombre_potions , adversaire
    elif vie_monstre <= 0:
        print("Monstre battu vous passez au niveau suivant : ")
        vie_monstre = 50
        nombre_potions += random.randint(1,3)
        vie_joueur += random.randint(25, 50)
        if vie_joueur > 50:
            vie_joueur = 50
        return True , vie_joueur , vie_monstre , nombre_potions , monstre[random.randint(0,3)]
    else:
        return True , vie_joueur , vie_monstre , nombre_potions , adversaire