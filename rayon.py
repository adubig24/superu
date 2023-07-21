import random
from pnj import PNJ
from data import Data

class Rayon:
    def __init__(self):
        self.__description = None
        self.__tresor = None
        self.__pnj=None

    def genere_contenu_rayon(self,caddie,liste_de_course):

        pile_ou_face = random.choice([True, False])
        inventaire=liste_de_course.liste_restante(caddie)
        random.shuffle(inventaire)
        if pile_ou_face:
            self.__tresor = inventaire[0]
            self.__description = Data.generer_bon_rayon(self.__tresor.get_nom())
        else:
            self.__pnj, self.__description = Data.generer_mauvais_rayon(inventaire)
            self.__pnj=PNJ(self.__pnj[0],self.__pnj[1],self.__pnj[2],self.__pnj[3],self.__pnj[4])

    def get_pnj(self):
        return self.__pnj

    def set_pnj(self,pnj):
        self.__pnj=PNJ(pnj[0],pnj[1],pnj[2],pnj[3],pnj[4])

    def get_tresor(self):
        if self.__tresor != None:
            return self.__tresor
        else:
            return None

    def get_description(self):
        return "\n"+self.__description
    
    def set_description(self, description):
        self.__description = description
