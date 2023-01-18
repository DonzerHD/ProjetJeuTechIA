def affichage():
    pass

def attaquer(vie):
    pass

def les_potions():
    pass

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
    pass
