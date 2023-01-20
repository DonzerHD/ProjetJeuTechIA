import random
import pandas as pd
import colorama
from colorama import Fore, Back, Style

# Faire les try catch
# Finir le csv
# Couleur console
# Signature des fonctions

def ajouter_couleur(couleur, message):
    print(couleur + message + Style.RESET_ALL)

def afficher_tableau_scores():
    """
    La fonction afficher_tableau_scores() lit les données d'un fichier CSV et les affiche sous forme de tableau.

    Args:
    nom_fichier (str): nom du fichier CSV contenant les scores

    Returns:
    None
    """

    # Lire les données à partir du fichier CSV
    scores = pd.read_csv("scores.csv")

    # Afficher le tableau des scores
    print(scores)


def score(nombre_victoire : int, vie_monstre : int, pseudo_utilisateur :int) -> int:
    """Cette fonction permet de mettre à jour le score d'un utilisateur dans un fichier CSV. 
    Si l'utilisateur existe déjà, son score est incrémenté d'une unité. 
    Sinon, un nouvel utilisateur est ajouté avec un score initial de 1.

    Args:
        nombre_victoire (int): Le nombre de victoires de l'utilisateur.
        vie_monstre (int): La vie restante du monstre.
        pseudo_utilisateur (str): Le pseudo de l'utilisateur.

    Returns:
        int: Le nombre de victoires de l'utilisateur mis à jour.
    """
    if vie_monstre <= 0:
        df = pd.read_csv('scores.csv')
        if pseudo_utilisateur in df['Pseudo'].values:
            user_index = df.index[df['Pseudo'] == pseudo_utilisateur][0]
            nombre_victoire = df.at[user_index, 'score']+1
            df.at[user_index, 'score'] = nombre_victoire
        else:
            df = df.append({'Pseudo': pseudo_utilisateur, 'score': nombre_victoire+1}, ignore_index=True)
            nombre_victoire += 1
        df.to_csv('scores.csv', index=False)
    return nombre_victoire

    
def affichage(vie_joueur: int, vie_monstre: int , nombre_potions : int, joueur_nom: str, monstre_nom: str, nombre_victoire: int):  
    """
    La fonction affichage() affiche l'état actuel du joueur, du monstre et du nombre de potions disponibles.

    Args:
    vie_joueur (int): la vie actuelle du joueur
    vie_monstre (int): la vie actuelle du monstre
    nombre_potions (int): le nombre de potions disponibles pour le joueur
    """   
    ajouter_couleur(Fore.BLUE,"="*85)
    print("Héros","[",joueur_nom,"]",":",vie_joueur,"PV","|","Méchants","[", monstre_nom,"]", ":",vie_monstre ,"PV","|","Potions",":",nombre_potions ," Score ",":", nombre_victoire)
    ajouter_couleur(Fore.BLUE,"="*85)

def attaquer(vie_personne_attaquee:int) -> int:
    """
    La fonction attaquer() simule une attaque contre une personne. Elle génère aléatoirement des dégâts infligés par l'attaque et affiche un message en conséquence.
    Args:
    vie_personne_attaquee (int): la vie actuelle de la personne qui subit l'attaque.
    Returns:
    int : la vie mise à jour de la personne après l'attaque.
    """
    degat = random.randint(0, 10)
    if degat > 7:
        ajouter_couleur(Fore.RED,"coup critique")
    elif degat < 7 and degat > 0:
        print("coup normal")
    elif degat == 0:
        ajouter_couleur(Fore.CYAN,"Esquive")
    vie_personne_attaquee = vie_personne_attaquee - degat 
    return vie_personne_attaquee
    


def les_potions(vie_joueur: int, vie_monstre: int, nombre_potions: int):
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

def choix_du_joueur(vie_joueur: int, vie_monstre: int, nombre_potions: int):
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

def verification_victoire_defaite(vie_joueur: int, vie_monstre: int, nombre_potions: int, monstre: list[str] , adversaire: str):
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
        afficher_tableau_scores()
        return False , vie_joueur , vie_monstre , nombre_potions , adversaire
    elif vie_monstre <= 0:
        ajouter_couleur(Fore.GREEN,"VICTOIRE ! Vous passez au niveau suivant ! ")
        vie_monstre = 50
        nombre_potions += random.randint(1,3)
        vie_joueur += random.randint(25, 50)
        if vie_joueur > 50:
            vie_joueur = 50
        return True , vie_joueur , vie_monstre , nombre_potions , monstre[random.randint(0,3)]
    else:
        return True , vie_joueur , vie_monstre , nombre_potions , adversaire