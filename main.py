vie_joueur = 50
vie_monstre = 50

def affichage():
    pass

def attaquer(vie):
    pass

def les_potions():
    pass

def choix_du_joueur():
    pass

def verification_vitoire_defaite(vie, partie_en_cours):
    pass

def attaque_bot():
    pass


partie_en_cours = True
while True:
    affichage(vie_joueur,vie_monstre)
    choix_du_joueur(vie_joueur,vie_monstre)
    verification_vitoire_defaite(vie_monstre, partie_en_cours)
    affichage(vie_joueur,vie_monstre)
    attaque_bot(vie_joueur)
    verification_vitoire_defaite(vie_monstre, partie_en_cours)