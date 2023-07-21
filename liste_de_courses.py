from data import Data

class Liste_de_courses:

    def __init__(self):
        self.__liste_de_course = Data.lister_random()
    
    def liste_restante(self, caddie):
        inventaire=caddie.get_inventaire()
        restant=self.__liste_de_course.copy()

        for item in self.__liste_de_course:
            if item in inventaire:
                restant.remove(item)
        return restant
    
    def get_liste_de_courses(self):
        return self.__liste_de_course