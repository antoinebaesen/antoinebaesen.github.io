#--- HDR ---#
# Code Python éxécuté sans être montré à l'élève
#--- HDR ---#


class abr():
    """ Classe représentant un arbre binaire de recherche """

    def __init__(self, valeur, gauche=None, droit=None):
        """ Constructeur de la classe """
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

    def __repr__(self):
        """ Méthode d'affichage de la classe """
        return "abr(" + repr(self.valeur) + ", " + repr(self.gauche) + ", " + repr(self.droit) + ")"

    def __str__(self):
        """ Méthode d'affichage de la classe """
        return "abr(" + str(self.valeur) + ", " + str(self.gauche) + ", " + str(self.droit) + ")"

    def ajouter(self, valeur):
        """ Ajoute la valeur dans l'arbre """
        if valeur < self.valeur:
            if self.gauche is None:
                self.gauche = abr(valeur)
            else:
                self.gauche.ajouter(valeur)
        elif valeur > self.valeur:
            if self.droit is None:
                self.droit = abr(valeur)
            else:
                self.droit.ajouter(valeur)

    def afficher(self):
        """ Affiche l'arbre """
        if self.gauche is not None:
            self.gauche.afficher()
        print(self.valeur)
        if self.droit is not None:
            self.droit.afficher()

    def contient(self, valeur):
        """ Renvoie True si la valeur est dans l'arbre """
        if valeur == self.valeur:
            return True
        elif valeur < self.valeur:
            if self.gauche is None:
                return False
            else:
                return self.gauche.contient(valeur)
        else:
            if self.droit is None:
                return False
            else:
                return self.droit.contient(valeur)

    def taille(self):
        """ Renvoie la taille de l'arbre """
        if self.gauche is None and self.droit is None:
            return 1
        elif self.gauche is None:
            return 1 + self.droit.taille()
        elif self.droit is None:
            return 1 + self.gauche.taille()
        else:
            return 1 + self.gauche.taille

arbre = abr(5)
arbre.ajouter(2)
arbre.ajouter(4)
arbre.afficher()
