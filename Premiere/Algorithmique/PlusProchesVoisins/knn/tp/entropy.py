from math import log


def occurrences(data: list, attr: str) -> dict:
    """
    :param data: (list) an example list
    :param att: (str) an attribute
    :return: (dict) dict of occ for the unique att values
    """
    dico = dict()
    for row in data:
        classe = row[attr]
        if classe in dico:
            dico[classe] += 1
        else:
            dico[classe] = 1
    return dico


def entropy(data: list, class_attr: str) -> float:
    """
    :param data: (list of dict) an example list
    :param class_attr: (str) the class attibute
    :return: (float) the entropy
    """
    dico = occurrences(data, class_attr)
    total = sum(dico.values())
    return sum( -n/total * log(n/total, 2) for n in dico.values() )


def gain(data: list, clusters: list, class_attr: str) -> float:
    """
    compute the gain in entropy. This is the entropy minus 
    mean of entropy for each clusters

    :param data: (list of dict) an example list
    :param clusters: (list) a list of examples clusters
    :param class_attr: (str) class attribute
    :return: (float) gain in entropy
    """
    gain = entropy(data, class_attr)
    for cl in clusters:
        sub_ent = entropy(cl, class_attr)
        gain -= (len(cl)/len(data))*sub_ent
    return gain
