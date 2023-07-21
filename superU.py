from caddie import Caddie
from rayon import Rayon
from data import Data
from data import formatter_reponses_gpt
from liste_de_courses import Liste_de_courses
from settings import *

def niveau_rayon(joueur, liste_de_courses):
    rayon=Rayon()
    rayon.genere_contenu_rayon(joueur, liste_de_courses)
    formatter_reponses_gpt(rayon.get_description())
    if rayon.get_tresor()!=None:
        print(f"\nVous obtenez l'item suivant : {rayon.get_tresor().get_nom()}\nFélicitations !")
        joueur.item_trouve(rayon.get_tresor())
    else:
        print(f"\nVous rencontrez {rayon.get_pnj().get_nom()} :")
        rayon.get_pnj().set_discussion(Data.generer_texte_pnj(rayon))
        formatter_reponses_gpt(" - "+rayon.get_pnj().get_discussion())
        rayon.get_pnj().rencontre(joueur, rayon)

def caisse(joueur):
    if joueur.get_argent() > PRIX_CADDIE:
        print(f"\nVous avez gagné ! Vous avez {joueur.get_argent()-PRIX_CADDIE} € de rab.")
        return True
    else:
        print("\nVous n'avez pas assez d'argent, vous allez devoir essayer de vous échapper par l'arrière.")
        return arriere_boutique(joueur)

def arriere_boutique(joueur):
    if joueur.get_nombre_de_gardes_vaincus()>3:
        print("Vous avez déjà vaincus tous les gardes, la voie est libre !")
        return True
    else:
        boss=Rayon()
        boss.set_pnj(Data.generer_pnj(True))
        boss.get_pnj().set_discussion("\nGarde - \"HALTE LÀ, client !!! Cette zone est reservée aux employés.\nVous ne comptiez tout de même pas partir sans payer, n'est-ce pas ?\"")
        boss.set_description("Une arrière boutique de Super U offre un espace de stockage organisé avec des étagères bien rangées pour les produits en attente de réapprovisionnement. On y trouve également une zone de préparation des commandes en vue de leur livraison aux clients ou aux rayons du magasin principal. L'arrière boutique permet une gestion efficace des stocks et une fluidité des opérations en coulisses.")
        print(boss.get_pnj().get_discussion())
        nombre_de_combats = 3-joueur.get_nombre_de_gardes_vaincus()
        print(f"\nVous avez {nombre_de_combats} gardes à vaincre.")
        for i in range(nombre_de_combats):
            print(f"Garde n°{i+1} : \n")
            boss.get_pnj().rencontre(joueur,boss)
            if joueur.get_argent()==0:
                perdu()
                termine=True
                return termine
            

def strike(text):
    return "".join([u'\u0336{}'.format(c) for c in text])

def perdu():
    print("\nAprès une dure journée, tu rentres chez toi bredouille. Sans AUCUNE courses et en ayant perdu ton argent.\nTa femme va t'engueuler...                            Encore...")

def main():
    print(f"Bienvenue dans votre Magasin Super U !\nVous avez pour objectif de parcourir les rayons afin de trouve tout ce qu'il y a dans votre liste de course.\nVous devez cependant garder au moins {PRIX_CADDIE}€ afin de payer vos courses, sinon il faudra tenter de forcer le chemin par l'arrière.\nVous commencez avec {ARGENT_DE_BASE}€ !")
    termine = False
    nom = input("Entrez votre nom : ")
    joueur = Caddie(nom)
    liste_de_courses = Liste_de_courses()
    print(f"\nVoici la liste de courses : \n")
    for i in liste_de_courses.get_liste_de_courses():
        if i in joueur.get_inventaire():
            print(strike(i.get_nom()))
        else:
            print(i.get_nom())
    boss=0
    phrase1="Aller au prochain rayon"
    while not termine:
        if joueur.get_argent==0:
            perdu()
            termine=True
        if len(joueur.get_inventaire())==len(liste_de_courses.get_liste_de_courses()):
            print("\nVous possédez maintenant tous les items de votre liste !\n")
            boss=1
            phrase1="Passer en caisse"
        choix=int(input(f"\nMenu de {joueur.get_nom()} : \n1 - {phrase1}\n2 - Voir votre poids\n3 - Voir votre inventaire\n4 - Voir votre liste de courses\n5 - Voir votre argent\n6 - Quitter\nChoix : "))
        if choix == 1:
            if boss==0:
                niveau_rayon(joueur, liste_de_courses)
            elif boss==1:
                termine=caisse(joueur)
        if choix == 2:
            print(f"\nLe poids de votre caddie est de {joueur.get_poids()}")
        if choix == 3:
            print(f"\nVoici la liste des items dans votre inventaire : ")
            for i in joueur.get_inventaire():
                print(i.get_nom())
        if choix == 4:
            print(f"\nVoici la liste de courses : ")
            for i in liste_de_courses.get_liste_de_courses():
                if i in joueur.get_inventaire():
                    print(strike(i.get_nom()))
                else:
                    print(i.get_nom())
        if choix == 5:
            print(f"Vous possédez {joueur.get_argent()} €")
        if choix == 6:
            termine=True
            print("\nAu revoir !\n")

if __name__=="__main__":
    main()