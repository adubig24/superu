from connexion_bdd import Connexion_bdd
from api_gpt import API_GPT
from item import Item
import random
import nltk

class Data:

    def lister_random():

        tous_les_objets = []

        cursor = Connexion_bdd.connexion()
        query = "SELECT nom FROM items"
        cursor.execute(query)

        for item in cursor :
            tous_les_objets.append(Item(item[0]))

        Connexion_bdd.deconnexion()

        random.shuffle(tous_les_objets)
        NOMBRE_D_ITEMS = int(input("Choisissez le nombre d'items à mettre dans la liste : "))
        return tous_les_objets[0:NOMBRE_D_ITEMS]
    
    def generer_texte_pnj(rayon):
        return  API_GPT.demande_GPT(f"Tu es {rayon.get_pnj().get_nom()}, tu te trouve dans ce rayon : {rayon.get_description()}. Ta personnalité est la suivante : {rayon.get_pnj().get_description()} - C'est un PNJ de type {rayon.get_pnj().get_type()} - Tu vas rencontrer le joueur principal, un être normal faisant ses courses au supermarché. Génère moi une réponse en 3 lignes en fonction de ta personnalité mentionnée plus tôt.")
    
    def generer_pnj(garde=False):

        cursor = Connexion_bdd.connexion()

        if garde==False:
            pnj_random=random.randint(1,41)
            query = f"SELECT nom,comportement,type,valeur,poids FROM pnj WHERE id={pnj_random}"
        else:
            query = f"SELECT nom,comportement,type,valeur,poids FROM pnj WHERE id=2"

        cursor.execute(query)
        reponse=cursor.fetchone()
        pnj=[reponse[0],reponse[1],reponse[2],reponse[3],reponse[4]]

        Connexion_bdd.deconnexion()

        return pnj

    def generer_mauvais_rayon(liste):
        pnj=Data.generer_pnj()
        return pnj, API_GPT.demande_GPT(f"Fais moi la description d'un rayon de supermarché type super U. Utilise le style d'un rapport de police, mais ne le précise pas. Il est important que le rayon est un rayon ou l'on ne puisse pas trouver : {[i.get_nom() for i in liste]}. Précise au début le nom du rayon. Décris certain aspects du rayon, ainsi que d'autres articles qui s'y trouvent en plus de celui mentionné plus tôt. La description sera précise et burlesque, et elle ne dépassera strictement pas 4 lignes.")

    def generer_bon_rayon(item):
        return API_GPT.demande_GPT(f"Fais moi la description d'un rayon de supermarché type super U. Utilise le style d'un rapport de police, mais ne le précise pas. Il est important que le rayon est un rayon ou l'on peut trouver : {item}. Précise au début le nom du rayon. Décris certain aspects du rayon, ainsi que d'autres articles qui s'y trouvent en plus de celui mentionné plus tôt. La description sera précise et burlesque, et elle ne dépassera strictement pas 4 lignes.")
    
    def generer_negociation_reussie(rayon):
        return API_GPT.demande_GPT(f"Tu es {rayon.get_pnj().get_nom()}, tu te trouve dans ce rayon : {rayon.get_description()}. Ta personnalité est la suivante : {rayon.get_pnj().get_description()} - C'est un PNJ de type {rayon.get_pnj().get_type()} - Tu as rencontré le joueur principal, un être normal faisant ses courses au supermarché. Voici ce que toi, {rayon.get_pnj().get_nom()} a dit au joueur : {rayon.get_pnj().get_discussion()}. Le joueur a alors voulu te convaincre de le laisser tranquille. Cependant, le joueur vient de réussir à te persuader de le laisser tranquille ! Imagine la réponse à des arguments qui t'ont définitivement convaincus !")
    
    def generer_negociation_ratee(rayon):
        return API_GPT.demande_GPT(f"Tu es {rayon.get_pnj().get_nom()}, tu te trouve dans ce rayon : {rayon.get_description()}. Ta personnalité est la suivante : {rayon.get_pnj().get_description()} - C'est un PNJ de type {rayon.get_pnj().get_type()} - Tu as rencontré le joueur principal, un être normal faisant ses courses au supermarché. Voici ce que toi, {rayon.get_pnj().get_nom()} a dit au joueur : {rayon.get_pnj().get_discussion()}. Le joueur a alors voulu te convaincre de le laisser tranquille. Le joueur vient de misérablement échouer à te convaincre. Imagine la réponse à des arguments qui ne t'ont définitivement pas convaincus !")
def formatter_reponses_gpt(reponse):
    nltk.download('punkt', quiet=True)
    sent_tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
    phrases = sent_tokenizer.tokenize(reponse)
    for phrase in phrases:
        print(phrase)