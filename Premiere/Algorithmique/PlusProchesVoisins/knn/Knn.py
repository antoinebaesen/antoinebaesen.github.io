import matplotlib.pyplot as plt
import graphviz as gv
import sys

from KnnOutils import MethodeDistance
from KnnClasses import KnnElement, KnnDinosaure, KnnTuple

def trouveVoisins(k: int, donnees: [KnnElement], nouvelle_donnee: KnnElement, methode: MethodeDistance = None) -> [KnnElement]:
    """
    Fonction qui permet de trouver les k plus proches voisins d'une nouvelle donnee parmi une liste de donnees de reference
    
    Parametres :
        k : (int) nombre de voisins a considerer
        donnees : ([KnnElement]) liste de donnees de référence
        nouvelle_donnee : (KnnElement) donnee a classifier
        methode : (MethodeDistance) methode de calcul de distance a utiliser

    Retour :
        ([KnnElement]) liste des k plus proches voisins

    Exemple :
        >>> trouveVoisins(3, [KnnNumber(1, 0), KnnNumber(2, 1), KnnNumber(3, 1), KnnNumber(4, 0)], KnnNumber(2, 0))
        [KnnNumber(1, 0), KnnNumber(4, 0), KnnNumber(3, 1)]

    CU :
        - k > 0
        - len(donnees) > k
        - len(nouvelle_donnee) == len(donnees[0])

    """
    if methode == None:
        methode = nouvelle_donnee.methodeDeBase()

    # On calcule les distances entre la nouvelle donnee et les donnees de reference
    distances : [(float, KnnElement)] = []

    for d in donnees:
        distances.append((d.distance(nouvelle_donnee, methode), d))

    # On trie les distances par ordre croissant
    distances.sort(key=lambda x: x[0])

    # On retourne les k plus proches voisins
    return [d[1] for d in distances[:k]]

def classeMajoritaire(voisins: [KnnElement]) :
    """
    Fonction qui permet de trouver la classe majoritaire parmi une liste de voisins
    
    Parametres :
        voisins : ([KnnElement]) liste de voisins

    Retour :
        La classe majoritaire parmi les voisins

    Exemple :
        >>> classeMajoritaire([KnnNumber(1, 0), KnnNumber(4, 0), KnnNumber(3, 1)])
        0

    CU :
        - len(voisins) > 0

    """
    # classes : {classe : int}
    classes = {}

    # On compte le fois ou chaque classe apparait dans la liste de voisins
    for v in voisins:
        if v.getClasse() in classes:
            classes[v.getClasse()] += 1
        else:
            classes[v.getClasse()] = 1

    # On retourne la classe majoritaire
    return max(classes, key=classes.get)

def knn(k: int, donnes : [KnnElement], nouvelle_donnee: KnnElement, methodeDistance: MethodeDistance = None):
    """
    Fonction qui détermine la classe d'une nouvelle donnee parmi une liste de donnees de reference

    Parametres :
        k : (int) nombre de voisins a considerer
        donnees : ([KnnElement]) liste de donnees de référence
        nouvelle_donnee : (KnnElement) donnee a classifier
        methodeDistance : (MethodeDistance) methode de calcul de distance a utiliser

    Retour :
        La classe de la nouvelle donnee

    Exemple :
        >>> knn(3, [KnnNumber(1, 0), KnnNumber(2, 1), KnnNumber(3, 1), KnnNumber(4, 0)], KnnNumber(2, 0))
        0

    CU :
        - k > 0
        - len(donnees) > k
        - len(nouvelle_donnee) == len(donnees[0])
    """

    # On récupère les k plus proches voisins de la nouvelle donnee
    voisins = trouveVoisins(k, donnes, nouvelle_donnee, methodeDistance)

    # On récupère la classe majoritaire parmi les voisins
    classe = classeMajoritaire(voisins)

    return classe

def ajouterAuxDonnees(k: int, donnees: [KnnElement], nouvelle_donnee: KnnElement, methodeDistance: MethodeDistance = None) -> [KnnElement]:
    """
    Fonction qui permet de classifier des donnees avec la methode des k plus proches voisins
    
    Parametres :
        k : (int) nombre de voisins a considerer
        donnees : ([KnnElement]) liste de donnees de référence
        nouvelle_donnee : (KnnElement) donnee a classifier
        methodeDistance : (MethodeDistance) methode de calcul de distance a utiliser

    Retour :
        La nouvelle liste de donnees avec la nouvelle donnee ajoutee
    
    Exemple :
        >>> ajouterAuxDonnees(3, [((1, 2), 0), ((3, 4), 1), ((5, 6), 1), ((7, 8), 0)], (2, 3))
        0

    CU :
        - k > 0
        - len(donnees) > k
        - len(nouvelle_donnee) == len(donnees[0][0])

    """
    # On calcule la classe de la nouvelle donnee et on l'affecte a la nouvelle donnee
    nouvelle_donnee.setClasse(knn(k, donnees, nouvelle_donnee, methodeDistance))
    # On ajoute la nouvelle donnee a la liste de donnees
    donnees.append(nouvelle_donnee)

    return donnees

def afficherDatasetTimed(dataset: [KnnElement]):
    """
    Fonction qui permet d'afficher un dataset de donnees
    """
    import random

    plt.clf()
    for d in dataset:
        # Pour chaque donnee, on affiche un point de la couleur de sa classe
        # La couleur est définie par un tuple de 3 valeurs entre 0 et 1
        #plt.scatter(d.getValeur()[0], d.getValeur()[1], c=d.getClasse())
        couleur = "g" if d.getClasse() == 'o' else "b" if d.getClasse() == '^' else "r"
        plt.scatter(d.getValeur()[0], d.getValeur()[1], marker=d.getClasse(), c=couleur)
        plt.show(block=False)
        plt.pause(0.1)
    plt.show()

def afficherDataset(dataset: [KnnElement]):
    """
    Fonction qui permet d'afficher un dataset de donnees
    """
    import random
    import matplotlib.colors as color

    plt.clf()
    for d in dataset:
        # Pour chaque donnee, on affiche un point de la couleur de sa classe
        # La couleur est définie par un tuple de 3 valeurs entre 0 et 1
        #plt.scatter(d.getValeur()[0], d.getValeur()[1], c=d.getClasse())

        couleur = "g" if d.getClasse() == 'o' else "b" if d.getClasse() == '^' else "r"
        plt.scatter(d.getValeur()[0], d.getValeur()[1], marker=d.getClasse(), c=couleur)
    plt.show()

def main():
    args : [str] = sys.argv[1:]

    func = "test"
    
    k = 3
    methode = None

    if(len(sys.argv) > 1):
        k = int(sys.argv[1])
    if(len(sys.argv) > 2):
        methode = MethodeDistance(sys.argv[2])
    
    print(knn(k, [KnnTuple((1, 2), 0), KnnTuple((3, 4), 1), KnnTuple((5, 6), 1), KnnTuple((7, 8), 0)], KnnTuple((2, 3), 1), methode))
    
if __name__ == "__main__":
    main()

