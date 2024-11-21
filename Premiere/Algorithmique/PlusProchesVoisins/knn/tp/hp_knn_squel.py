from distances import *
from classification_common import *

USED_ATT = ['Sagesse', 'Loyaute', 'Courage', 'Malice' ]
CLASS_ATT = 'Maison'


def normalise_eleve(e: dict, minmax: dict):
    """
    :param e: (dict) un étudiant 
    :param minmax: (dict) valeurs minimales et maximales pour chaque paramètre
    :return: (list) la liste des valeurs normalisées dans l'ordre de USED_ATT

    :Example:

    >>> minmax  = {'Loyaute': (2, 10), 'Nom': ('Adrian', 'Vincent'), 'Malice': (2, 10), 'Maison': ('Gryffondor', 'Serpentard'), 'Courage': (2, 10), 'Sagesse': (2, 10)}
    >>> hermione = {'Nom': 'Hermione', 'Courage': 8, 'Loyaute': 6, 'Sagesse': 6, 'Malice': 6}
    >>> normalise_eleve(hermione, minmax)
    [0.5, 0.5, 0.75, 0.5]
    """
    pass


def distance_eleve(e1: dict, e2: dict, minmax: dict):
    """
    :param e1: (dict) un élève 
    :param e2: (dict) un autre élève
    :return: (float) la distance de e1 à e2
    """
    pass


def choix_classe(datas: list)->str:
    """
    :param datas: (list of tuple) liste de couples (distance, classe)
    :return: une classe la plus présente dans les couples
    :CU: Aucune
    """
    pass


def knn(examples: list, k: int, eleve: dict):
    """
    :param examples: (list) une liste d'exemples
    :param k: (int) le nombre de voisin à considérer
    :param eleve: (dict) l'élève à classer
    :return: (str) la classe majoritaire chez les voisins
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)

def accuracy(training_examples: list, test_examples, k: int)->float:
    """
    :param training_examples: (list of dict) examples used to classify
    :param test_examples: (list of dict) examples used to calculates the accuracy
    :param k: (int) number of neighbors 
    :return: (float) percentage of bad classified examples
    """
    pass


def accuracy_range(examples: list, t: int)->tuple:
    """
    :param examples: (list of dict) examples
    :param k: (int) number of neighbors
    :param t: (int) an integer
    :return: (tuple) a range [l, r] at 95%
    :UC: t>1
    """
    pass
