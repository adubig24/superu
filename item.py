class Item:
    def __init__(self, nom):
        self.__nom = nom
    
    def get_nom(self):
        return self.__nom