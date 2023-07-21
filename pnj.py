from entite import Entite
from data import formatter_reponses_gpt
from data import Data
from settings import RAQUETTAGE_LEVEL
import random

class PNJ(Entite):
    def __init__(self, nom, description, type, argent, poids):
        super().__init__(poids, argent, nom)
        self.__description = description
        self.__type=type
        self.__discussion=None

    def get_discussion(self):
        return self.__discussion
    
    def set_discussion(self, discussion):
        self.__discussion = discussion

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__description
    
    def combattre(self, joueur):
        if joueur.pousser(self._poids) >= 0:
            print(f"\nVous dégommez {self._nom} de votre chemin.")
            if self._nom=="Garde":
                joueur.garde_vaincu()
        else:
            print(f"\nVous ne parvenez pas à écraser {self._nom}. Il vous vole 1 item et {abs(self._argent)}€ !")
            raquetter=joueur.set_argent(-abs(self._argent))
            if raquetter:
                print(f"\n{self._nom} vous détruit les dents, et vous vole tout votre argent.")
            joueur.item_perdu()

    def rencontre(self, joueur, rayon):
        if self.__type == "mechant":
            rencontre=None
            while rencontre!='termine':
                while True:
                    try:
                        choix=int(input("\nMenu :\n1 - Pousser\n2 - Soudoyer\n3 - Négocier(Chances de succès : 30%)\nChoix : "))
                        if choix in range(1,4):
                            break
                    except:
                        pass
                    print("\nVeuillez entrer un choix correct.")

                if choix==1:
                    self.combattre(joueur)
                    rencontre='termine'

                elif choix==2:
                    if joueur.get_argent() > abs(self._argent):
                        print(f"\nVous soudoyez {self._nom} afin d'être tranquille. Vous perdez {abs(self._argent)}€")
                        joueur.set_argent(self._argent)
                        rencontre='termine'
                    else:
                        print(f"Vous n'avez pas assez d'argent pour soudoyer {self._nom}.")

                elif choix==3:
                    print(f"\nVous tentez de convaincre {self._nom}.")
                    essai_convaincre=random.randint(1,100)
                    if essai_convaincre <=30:
                        formatter_reponses_gpt(Data.generer_negociation_reussie(rayon))
                        print(f"\nNégociation réussie ! {self._nom} passe son chemin et vous laisse tranquille.")
                    else:
                        formatter_reponses_gpt(Data.generer_negociation_ratee(rayon))
                        print(f"\nNégociation échouée. {self._nom} vous vole {abs(self._argent)+RAQUETTAGE_LEVEL}€.")
                        joueur.set_argent(self._argent-10)
                    rencontre='termine'

        elif self.__type == "gentil":
            print(f"\nVous gagnez {self._argent}€ et continuez votre chemin.\n")
            joueur.set_argent(self._argent)

        elif self.__type == "quete":
            while True:
                try:
                    choix=int(input("\nMenu :\n1 - Aider\n2 - Pousser\n3 - Ignorer\nChoix : "))
                    if choix in range(1,4):
                        break
                except:
                    pass
                print("\nVeuillez entrer un choix correct.")

            if choix==1:
                print(f"\n{self._nom} vous remercie et vous gagnez {self._argent}€\n")
                joueur.set_argent(self._argent)

            elif choix==2:
                self.combattre(joueur)
                print("Vous devriez avoir honte !\n")

            elif choix==3:
                print(f"\n{self._nom} se met à pleurer mais vous continuez votre chemin, tel le sans-coeur que vous êtes.\n")

        

