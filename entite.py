class Entite:
    def __init__(self, poids = 1, argent = None, nom = None):
        self._poids = poids
        self._argent = argent
        self._nom = nom
    
    def get_nom(self):
        return self._nom
    
    def set_nom(self):
        return self._nom
    
    def get_poids(self):
        return self._poids
    
    def set_poids(self, poids):
        self._poids = poids

    def set_argent(self, somme_modifiee):
        self._argent += somme_modifiee
        if self._argent<0:
            self._argent=0
            return True
        else:
            return False
    
    def get_argent(self):
        return self._argent