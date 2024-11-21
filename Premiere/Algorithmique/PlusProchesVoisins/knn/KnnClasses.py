from KnnOutils import MethodeDistance
import matplotlib.pyplot as plt
import graphviz as gv

class KnnElement():
    def __init__(self, valeur, classe):
        self.valeur = valeur
        self.classe = classe

    def __str__(self):
        return f"KnnElement({self.valeur}, {self.classe})"
    
    def __repr__(self):
        return f"[{self.classe}]"
    
    def getClasse(self):
        return self.classe
    
    def getValeur(self):
        return self.valeur
    
    def setClasse(self, classe):
        self.classe = classe

    def methodeDeBase(self):
        return None
    
    def distance(self, other, methode: MethodeDistance = None):
        if methode == None:
            return self.methodeDeBase()

        if methode == MethodeDistance.EUCLIDIENNE:
            return self.distanceEuclidienne(other)
        elif methode == MethodeDistance.MANHATTAN:
            return self.distanceManhattan(other)
        elif methode == MethodeDistance.MINKOWSKI:
            return self.distanceMinkowski(other)
        elif methode == MethodeDistance.HAMMING:
            return self.distanceHamming(other)
        else:
            raise Exception("Methode de distance inconnue")

    def distanceEuclidienne(self, other):
        pass

    def distanceManhattan(self, other):
        pass

    def distanceMinkowski(self, other):
        pass

    def distanceHamming(self, other):
        pass

class KnnNumber(KnnElement):
    def __init__(self, valeur, classe):
        super().__init__(valeur, classe)

    def distanceManhattan(self, other):
        return abs(self.valeur - other.valeur)
    
    def distanceEuclidienne(self, other):
        return self.distanceManhattan(other)
    
    def distanceMinkowski(self, other):
        return self.distanceManhattan(other)
    
    def distanceHamming(self, other):
        return 1 if self.valeur != other.valeur else 0
    
    def methodeDeBase(self):
        return MethodeDistance.MANHATTAN
    
class KnnTuple(KnnElement):
    def __init__(self, valeur, classe):
        super().__init__(valeur, classe)

    def distanceEuclidienne(self, other):
        return ((self.valeur[0] - other.valeur[0])**2 + (self.valeur[1] - other.valeur[1])**2)**0.5

    def distanceManhattan(self, other):
        return abs(self.valeur[0] - other.valeur[0]) + abs(self.valeur[1] - other.valeur[1])

    def distanceMinkowski(self, other):
        return (abs(self.valeur[0] - other.valeur[0])**3 + abs(self.valeur[1] - other.valeur[1])**3)**(1/3)
    
    def distanceHamming(self, other):
        total = 0
        for i in range(len(self.valeur)):
            if self.valeur[i] != other.valeur[i]:
                total += 1
        return total
    
    def methodeDeBase(self):
        return MethodeDistance.EUCLIDIENNE

class KnnStr(KnnElement):
    def __init__(self, valeur, classe):
        super().__init__(valeur, classe)

    def distanceEuclidienne(self, other):
        total = 0
        for i in range(len(self.valeur)):
            total += (ord(self.valeur[i]) - ord(other.valeur[i]))**2
        return total**0.5
    
    def distanceManhattan(self, other):
        total = 0
        for i in range(len(self.valeur)):
            total += abs(ord(self.valeur[i]) - ord(other.valeur[i]))
        return total
    
    def distanceMinkowski(self, other):
        total = 0
        for i in range(len(self.valeur)):
            total += abs(ord(self.valeur[i]) - ord(other.valeur[i]))**3
        return total**(1/3)
    
    def distanceHamming(self, other):
        total = 0
        for i in range(len(self.valeur)):
            if self.valeur[i] != other.valeur[i]:
                total += 1
        return total
    
    def methodeDeBase(self):
        return MethodeDistance.HAMMING
    
class KnnList(KnnElement):
    def __init__(self, valeur, classe):
        super().__init__(valeur, classe)

    def distanceEuclidienne(self, other):
        total = 0
        for i in range(len(self.valeur)):
            total += (self.valeur[i] - other.valeur[i])**2
        return total**0.5
    
    def distanceManhattan(self, other):
        total = 0
        for i in range(len(self.valeur)):
            total += abs(self.valeur[i] - other.valeur[i])
        return total
    
    def distanceMinkowski(self, other):
        total = 0
        for i in range(len(self.valeur)):
            total += abs(self.valeur[i] - other.valeur[i])**3
        return total**(1/3)
    
    def distanceHamming(self, other):
        total = 0
        for i in range(len(self.valeur)):
            if self.valeur[i] != other.valeur[i]:
                total += 1
        return total
    
    def methodeDeBase(self):
        return MethodeDistance.EUCLIDIENNE

class KnnDinosaure(KnnElement):
    def __init__(self, valeur, classe, descendants = []):
        super().__init__(valeur, classe)
        self.descendants = descendants
        self.origine = None
        for d in descendants:
            d.setOrigine(self)

    def setOrigine(self, origine):
        self.origine = origine

    def __str__(self):
        return f"{self.valeur} [{self.classe}]"
    
    def aDesDescendants(self):
        return len(self.descendants) > 0
    
    def getDescendants(self):
        return self.descendants
    
    def getOrigine(self):
        if(self.origine == None):
            return self
        else:
            return self.origine.getOrigine()
        
    def getOrigines(self):
        if(self.origine == None):
            return [self]
        else:
            return [self] + self.origine.getOrigines()

    def origineCommune(self, other):
        originesA = self.getOrigines()
        originesB = other.getOrigines()
        for i in range(len(originesA)):
            for j in range(len(originesB)):
                if originesA[i] == originesB[j]:
                    return originesA[i], abs(i+j)
        return None, None

    def distanceDansLarbre(self, other):
        origineCommune, distance = self.origineCommune(other)
        if origineCommune == None:
            return None
        else:
            return distance
        
    def afficherArbre(self, n = 0):
        print("  "*n, self)
        for d in self.descendants:
            d.afficherArbre(n+1)

    def afficherArbreGraphique(self, g, n = 0) -> gv.Digraph:
        g.node(str(self), str(self))
        for d in self.descendants:
            d.afficherArbreGraphique(g, n+1)
            g.edge(str(self), str(d))
        return g
        
    def distance(self, other, methode: MethodeDistance = None):
        return self.distanceDansLarbre(other)
    
    def methodeDeBase(self):
        return None
