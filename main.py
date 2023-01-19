from utils import affichage , choix_du_joueur , attaquer , verification_victoire_defaite , score
import random

vie_joueur = 50
vie_monstre = 50
nombre_potions = 3
monstre = ["Thomas" , "Dylan" , "Saber" , "Karim"]
joueur_nom = ["Charles" , "Antoine"]
nombre_victoire = 0


chiffre = random.randint(0,1)
index_monstre = random.randint(0,3)
adversaire = monstre[index_monstre]
partie_en_cours = True

pseudo_utilisateur = input("Quel est votre pseudo : ")
while partie_en_cours:
    affichage(vie_joueur, vie_monstre , nombre_potions, joueur_nom[chiffre], adversaire , nombre_victoire)
    print("coup joueur ou potion")
    vie_joueur , vie_monstre , nombre_potions= choix_du_joueur(vie_joueur, vie_monstre, nombre_potions)
    nombre_victoire = score(nombre_victoire, vie_monstre , pseudo_utilisateur)
    partie_en_cours, vie_joueur , vie_monstre , nombre_potions, adversaire= verification_victoire_defaite(vie_joueur, vie_monstre, nombre_potions, monstre , adversaire)
    affichage(vie_joueur, vie_monstre , nombre_potions, joueur_nom[chiffre], adversaire , nombre_victoire)
    print("Coup du monstre")
    vie_joueur = attaquer(vie_joueur)
    partie_en_cours , vie_joueur , vie_monstre , nombre_potions , adversaire = verification_victoire_defaite(vie_joueur, vie_monstre, nombre_potions , monstre , adversaire)
    
    
