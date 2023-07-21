import random
from settings import *
from entite import Entite

class Caddie(Entite):

    def __init__(self, nom):
        super().__init__(1, ARGENT_DE_BASE, nom)
        self.__liste_d_inventaire = []
        self.__nombre_de_gardes_vaincus = 0

    def get_inventaire(self):
        return self.__liste_d_inventaire
    
    def pousser(self, poids_adversaire):
        return self.get_poids() - poids_adversaire - random.randint(0, DIFFICULTE_DES_PNJ)

    def item_trouve(self, item):
        self.__liste_d_inventaire.append(item)
        self.set_poids(self.get_poids()+1)
    
    def item_perdu(self):
        if len(self.__liste_d_inventaire)>0:
            self.__liste_d_inventaire.pop()
            self.set_poids(self._poids-1)
        else:
            print("Vous n'aviez cependant pas d'items, donc vous êtes épargné cette fois.")
    
    def garde_vaincu(self):
        self.__nombre_de_gardes_vaincus+=1
    
    def get_nombre_de_gardes_vaincus(self):
        return self.__nombre_de_gardes_vaincus