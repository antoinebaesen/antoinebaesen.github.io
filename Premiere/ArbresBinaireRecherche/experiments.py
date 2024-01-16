import random
import matplotlib.pyplot as plt

class abr():
    def __init__(self, val):
        self.l = None
        self.r = None
        self.parent = None
        self.val = val

    def __str__(self):
        return self.repr()
    
    def repr(self, level=0, left=False):
        # use ─ and └ ┌
        # put required | and spaces
        
        s = ""
        if self.r != None:
            s += self.r.repr(level+1, True)

        s += "    " * level
        if level > 0:
            if left:
                s += "┌───"
            else:
                s += "└───"
        s += str(self.val) + "\n"

        if self.l != None:
            s += self.l.repr(level+1, False)

        return s
    
    def insert(self, val):
        if val < self.val:
            if self.l == None:
                self.l = abr(val)
                self.l.parent = self
            else:
                self.l.insert(val)
        else:
            if self.r == None:
                self.r = abr(val)
                self.r.parent = self
            else:
                self.r.insert(val)

    def racine(self):
        if self.parent == None:
            return self
        else:
            return self.parent.racine()

    def supp(self, val):
        # Si on a un fils gauche
        if(val < self.val and self.l != None):
            return self.l.supp(val)
        
        # Si on a un fils droit
        elif(val > self.val and self.r != None):
            return self.r.supp(val)
    
        # Si on est une feuille
        elif(self.l == None and self.r == None):
            if(self.val == val):
                self.parent.suppFils(self)
                return self
            else:
                return None
        else:
            if(self.val == val):
                nouvelleRacine = None
                childrens = self.getAllChilds()
                # Dans le cas où on a des enfants et on est la node a supprimer
                
                if(self.l != None):
                    nouvelleRacine = abr(self.l.val)
                elif(self.r != None):
                    nouvelleRacine = abr(self.r.val)

                if(nouvelleRacine != None):
                    childrens.remove(nouvelleRacine.val)

                    for i in childrens:
                        nouvelleRacine.insert(i)

                nouvelleRacine.parent = self.parent
                if(self.parent != None):
                    if(self.parent.l == self):
                        self.parent.l = nouvelleRacine
                    else:
                        self.parent.r = nouvelleRacine
                    
            
        

    def getAllChilds(self):
        listVal = []
        if self.l != None:
            listVal.append(self.l.val)
            listVal.extend(self.l.getAllChilds())
        if self.r != None:
            listVal.append(self.r.val)
            listVal.extend(self.r.getAllChilds())
        return listVal

    def suppsFils(self, fils):
        if(self.l == fils):
            self.l = None
        elif(self.r == fils):
            self.r = None

    def search(self, val):
        if val == self.val:
            return self
        elif val < self.val:
            if self.l == None:
                return None
            else:
                return self.l.search(val)
        else:
            if self.r == None:
                return None
            else:
                return self.r.search(val)
            
    def delete(self, val):
        node = self.search(val)
        if node == None:
            return
        if node.l == None and node.r == None:
            if node.parent.l == node:
                node.parent.l = None
            else:
                node.parent.r = None
        elif node.l == None:
            if node.parent.l == node:
                node.parent.l = node.r
            else:
                node.parent.r = node.r
        elif node.r == None:
            if node.parent.l == node:
                node.parent.l = node.l
            else:
                node.parent.r = node.l
        else:
            tmp = node.r
            while tmp.l != None:
                tmp = tmp.l
            node.val = tmp.val
            if tmp.parent.l == tmp:
                tmp.parent.l = None
            else:
                tmp.parent.r = None

    def min(self):
        if self.l == None:
            return self
        else:
            return self.l.min()
        
    def max(self):
        if self.r == None:
            return self
        else:
            return self.r.max()
        
    def insertAll(self, l):
        for i in l:
            self.insert(i)

    def hauteur(self):
        if self.l == None and self.r == None:
            return 0
        elif self.l == None:
            return 1 + self.r.hauteur()
        elif self.r == None:
            return 1 + self.l.hauteur()
        else:
            return 1 + max(self.l.hauteur(), self.r.hauteur())

def test_hauteur():
    tailles = []
    for i in range(100):
        arbres = []
        for j in range(1000):
            a = abr(random.randint(0, 100))
            a.insertAll([random.randint(0, 100) for _ in range(i)])
            arbres.append(a)
        moy = sum([a.hauteur() for a in arbres]) / len(arbres)
        tailles.append(moy)

    import matplotlib.pyplot as plt

    print(tailles)

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot([i for i in range(100)], tailles)

    # Set the labels and title
    ax.set_xlabel("Nombre d'éléments")
    ax.set_ylabel("Hauteur moyenne de l'arbre")
    ax.set_title("Hauteur moyenne d'un arbre binaire de recherche")

    # Show the grid
    ax.grid(True)

    # Show the plot
    plt.show()

class exprAbr(abr):

    def __init__(self, val, left=None, right=None):
        super().__init__(val)
        self.l = left
        self.r = right

    def __str__(self):
        res = ""
        if self.l != None:
            res += "(" + str(self.l)
        res += str(self.val)
        if self.r != None:
            res += str(self.r) + ")"
        return res
    
    def __strPostfix__(self):
        res = ""
        if self.l != None:
            res += self.l.__strPostfix__() + " "
        if self.r != None:
            res += self.r.__strPostfix__() + " "
        res += str(self.val)
        return res
    
    def eval(self):
        if self.val == "+":
            return self.l.eval() + self.r.eval()
        elif self.val == "-":
            return self.l.eval() - self.r.eval()
        elif self.val == "*":
            return self.l.eval() * self.r.eval()
        elif self.val == "/":
            return self.l.eval() / self.r.eval()
        else:
            return self.val

def parcoursLargeur(arbre : abr):
    res = []
    current = [arbre]
    while len(current) > 0:
        next = []
        for a in current:
            res.append(a.val)
            if a.l != None:
                next.append(a.l)
            if a.r != None:
                next.append(a.r)
        current = next
    return res

def creerArbreComplet(taille : int):
        res = abr(2 ** (taille - 1))
        for i in range (taille-2, 0, -1):
            for j in range (0, 2 ** (taille - 1 - i)):
                res.insert(j * 2 ** i + 2 ** (i - 1))
        return res



a = exprAbr("*", exprAbr("+", exprAbr(3), exprAbr(7)), exprAbr(2))
print(a)
print(a.eval())
print(a.__strPostfix__())

#arbreComplet = abr(10)
#arbreComplet.insertAll([i for i in range(20)])

arbreComplet = creerArbreComplet(5)

#print(arbreComplet)

arbreComplet.supp(12)
print(arbreComplet)