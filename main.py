from utils import affichage , les_potions , choix_du_joueur , attaquer , verification_vitoire_defaite

vie_joueur = 50
vie_monstre = 50
nombre_potions = 3


partie_en_cours = True
while partie_en_cours:
    affichage(vie_joueur, vie_monstre , nombre_potions)
    print("coup joueur ou potion")
    vie_joueur , vie_monstre , nombre_potions = choix_du_joueur(vie_joueur, vie_monstre, nombre_potions)
    partie_en_cours = verification_vitoire_defaite(vie_joueur, vie_monstre)
    affichage(vie_joueur, vie_monstre , nombre_potions)
    print("Coup du monstre")
    vie_monstre , vie_joueur = attaquer(vie_monstre, vie_joueur)
    partie_en_cours = verification_vitoire_defaite(vie_joueur, vie_monstre)