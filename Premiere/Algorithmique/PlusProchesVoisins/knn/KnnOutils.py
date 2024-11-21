from enum import Enum

class MethodeDistance(Enum):
    """ Enumeration des methodes de calcul de distance """
    EUCLIDIENNE = 1
    MANHATTAN = 2
    MINKOWSKI = 3
    HAMMING = 4
