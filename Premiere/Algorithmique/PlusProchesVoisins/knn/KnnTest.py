from Knn import *

def testCouleurs(k : int = 3, methodeDistance : MethodeDistance = None):
    """
    Fonction qui permet de tester la methode des k plus proches voisins sur des donnees de couleurs
    """

    import random

    dataset = []

    """
    for i in range (5):
        for j in range (5):
            dataset.append(KnnTuple((i*10, j*10), (i * 0.2, j * 0.2, 0)))
    """
    dataset.append(KnnTuple((10, 00), '^'))
    dataset.append(KnnTuple((11, 13), '^'))
    dataset.append(KnnTuple((12, 14), '^'))
    dataset.append(KnnTuple((40, 40), 'o'))
    dataset.append(KnnTuple((50, 50), 'o'))
    dataset.append(KnnTuple((60, 60), 'o'))
    dataset.append(KnnTuple((20, 20), 's'))
    dataset.append(KnnTuple((0, 10), 's'))
    dataset.append(KnnTuple((0, 0), 's'))
    afficherDataset(dataset)

    for i in range (200):
        dataset = ajouterAuxDonnees(k, dataset, KnnTuple((random.randint(0, 50), random.randint(0, 50)), None), methodeDistance)

    afficherDatasetTimed(dataset)

def testDinosaures():
    """
    donnees = [((1, 2), 0), ((3, 4), 1), ((5, 6), 1), ((7, 8), 0)]
    nouvelle_donnee = (2, 3)
    print(ajouterAuxDonnees(3, donnees, nouvelle_donnee))
    """

    poulet = KnnDinosaure("Poulet", -1)

    # On cree un arbre de dinosaures
    dinosaure10 = KnnDinosaure("Tyrannosaure", 1, [poulet])
    dinosaure9 = KnnDinosaure("Brachiosaure", 2)
    dinosaure8 = KnnDinosaure("Triceratops", 2)
    dinosaure7 = KnnDinosaure("Stegosaure", 2)
    dinosaure6 = KnnDinosaure("Velociraptor", 2, [dinosaure10, dinosaure9])
    dinosaure5 = KnnDinosaure("Diplodocus", 2, [dinosaure8, dinosaure7])
    dinosaure4 = KnnDinosaure("Allosaure", 1)
    dinosaure3 = KnnDinosaure("Carnosaure", 1, [dinosaure6, dinosaure4])
    dinosaure2 = KnnDinosaure("Iguanodon", 2, [dinosaure5])
    dinosaure1 = KnnDinosaure("Compsognathus", 2, [dinosaure3, dinosaure2])

    dinosaure1.afficherArbreGraphique(gv.Digraph(format='png'), 0).render('test-output/round-table.gv', view=True)
    print(dinosaure1.distance(dinosaure10))

    dataset = [dinosaure1, dinosaure2, dinosaure3, dinosaure4, dinosaure5, dinosaure6, dinosaure7, dinosaure8, dinosaure9, dinosaure10]
    # On va ajouter le poulet dans le dataset
    dataset = ajouterAuxDonnees(3, dataset, poulet)

    # On affiche le poulet nouvellement rangé
    print(poulet)

testCouleurs()
# testDinosaures()