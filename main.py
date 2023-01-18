from utils import affichage , les_potions , choix_du_joueur , attaquer , verification_vitoire_defaite

vie_joueur = 50
vie_monstre = 50


partie_en_cours = True
while True:
    affichage(vie_joueur,vie_monstre)
    choix_du_joueur(vie_joueur,vie_monstre)
    verification_vitoire_defaite(vie_monstre, partie_en_cours)
    affichage(vie_joueur,vie_monstre)
    verification_vitoire_defaite(vie_monstre, partie_en_cours)