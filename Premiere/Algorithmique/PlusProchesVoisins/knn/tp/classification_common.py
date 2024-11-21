# [[file:../tp_hp_knn.org::*Les données][Les données:1]]
import csv
from functools import reduce

def read_example_file(fname: str) -> list:
    """
    :param fname: (str) the filename
    :return: (list) list of example
    """
    res = list()
    for row in csv.DictReader(open(fname, 'r'),
                               delimiter=';'):
        for k, v in row.items():
            if v.isdigit():
                row[k] = int(v)
            elif v.isdecimal():
                row[k] = float(v)
        res.append(row)
    return res


def get_attributs(examples: list)->list:
    """
    :param examples: (list of dict) une liste d'exemples sous la forme 
                     de dictionnaires
    :return: (set) l'ensemble des attributs communs à tous les exemples
    """
    return reduce(lambda a, b: a.intersection(b),
                  map( lambda e: set(e.keys()), examples ))


def attributes_min_max(examples: list)->dict:
    """
    :param examples: (list of dict) une liste d'exemples sous la forme
                     de dictionnaires
    :return: (dict) un dictionnaire contenant, pour chaque attribut, un couple (min, max)
    """
    return { a: (reduce(min, map(lambda e: e[a], examples)),
                 reduce(max, map(lambda e: e[a], examples)))
             for a in get_attributs(examples) }
# Les données:1 ends here

# [[file:../tp_hp_knn.org::*regrouper les exemples][regrouper les exemples:1]]
def regroupe(exemples: list[dict], att: str) -> dict:
    """
    :param exemples: (list) une liste d'exemples
    :param att: (str) le nom d'un attribut
    :return: (dict) le dictionnaire des valeurs des attributs
    """
    res = {}
    for ex in exemples:
        k = ex[att]
        if k in res:
            res[k].append(ex)
        else:
            res[k] = [ ex ]
    return res
# regrouper les exemples:1 ends here
