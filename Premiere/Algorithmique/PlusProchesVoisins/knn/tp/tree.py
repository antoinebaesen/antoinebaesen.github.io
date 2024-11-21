"""
:mod: une classe pour représenter les arbres de décision
"""
import graphviz, time, hashlib
from criterion import Criterion

WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#FF0000'

def escape_str(obj):
    '''
    convertit l'objet obj en une chaîne de caractères ASCII
    fct utile pour méthode to_dot des BinaryTree
    '''
    chaine = str(obj)
    chaine_echap = ''
    for c in chaine:
        n = ord(c)
        if 32 <= n <= 126 and c != '"':
            chaine_echap += c
        else:
            chaine_echap += '\\x{:04X}'.format(n)
    return chaine_echap

class TreeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'TreeError, {0} '.format(self.message)
        else:
            return 'TreeError has been raised'

class Node:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return f'{self._value}'

class TestNode(Node):
    def __init__(self, crit: Criterion):
        self._crit = crit

    def criterion(self):
        return self._crit

    def __str__(self):
        return str(self._crit)


class BooleanTreeNode(Node):
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return 'T' if self._value else 'F'


class PrefixTreeNode(BooleanTreeNode):
    def __init__(self, value: bool, prefix: str):
        super().__init__(value)
        self.__prefix = prefix

    def __str__(self):
        return f"{self._value}-'{self.__prefix}'"


class Tree:
    def __init__(self, *args):
        """
        Tree constructor
        """
        if len(args) == 0:
            self.__content = ()
        elif len(args) == 3:
            if not isinstance(args[0], Node):
                raise TreeError(f'{args[0]} is not a node')
            if not isinstance(args[1], Tree):
                raise TreeError(f'{args[1]} is not a tree')
            if not isinstance(args[2], Tree):
                raise TreeError(f'{args[2]} is not a tree')
            self.__content = (args[0], args[1], args[2])
        else:
            raise TreeError('bad number of argument')

    def is_empty(self) -> bool:
        """
        :return: True iff self is an empty tree
        """
        return len(self.__content) == 0

    def left(self) -> "Tree":
        """
        :return: the sub left tree
        """
        if len(self.__content) == 0:
            raise TreeError()
        return self.__content[1]

    def right(self) -> "Tree":
        """
        :return: the sub right tree
        """
        if len(self.__content) == 0:
            raise TreeError()
        return self.__content[2]

    def root(self) -> Node:
        """
        :return: content of root node
        """
        if len(self.__content) == 0:
            raise TreeError()
        return self.__content[0]

    def is_leaf(self) -> bool:
        """
        :return: True iff the tree is a leaf
        """

        return ( (not self.is_empty()) and \
                 self.right().is_empty() and \
                 self.left().is_empty() )

    def __str__(self):
        if self.is_empty():
            return chr(0x0394)
        else:
            node = self.root()
            return "N({},{},{})".format(node,
                                        str(self.left()),
                                        str(self.right()))

    def __repr__(self):
        self.__fname = hashlib.sha1(self.__str__().encode()).hexdigest()
        return self.savefig(self.__fname)

    def _forest_helper(self):
        if self.is_empty():
            res = "[ ,phantom ]"
        else:
            node = self.root()
            if self.is_leaf():
                res = "[ {{\small {}}} ]".format(node)
            else:
                res = "[ {{\small {}}} {} {} ]".format(node,
                                                       str(self.left()._forest_helper()),
                                                       str(self.right()._forest_helper()))
        return res

    def append_bfs(self, x: Node):
        """
        append a node to the first available place in bfs order

        :param x: (Node) a node
        """
        q = []
        q.append(self)
        fini = False
        while q != [] and not fini:
            nc = q[0]
            del q[0]
            if nc.is_empty():
                fini = True
                nc.__content = [x, Tree(), Tree()]
            else:
                q.append(nc.left())
                q.append(nc.right())

    def toTikZ(self) -> str:
        """
        :return: a tikz representation of the tree
        """
        tikz_code = """
  \\begin{{forest}}
  for tree={{%
    s sep=.5cm,    
    where n=1{{ edge label = {{node[midway, above left, font=\scriptsize]{{0}}}} }}  {{ edge label = {{node[midway, above right, font=\scriptsize]{{1}}}} }}  }} %
  {}
  \\end{{forest}}"""
        return tikz_code.format(self._forest_helper())

    def to_dot(self, background_color=WHITE):
        '''
        renvoie une chaîne de caractères contenant la description au format dot de self.
        '''
        LIEN = '\t"N({:s})" -> "N({:s})" [color="{:s}", label="{:s}", fontsize="8"];\n'
        def aux(arbre, prefix=''):
            if arbre.is_empty():
                descr = '\t"N({:s})" [color="{:s}", label=""];\n'.format(prefix,
                                                                         background_color)
            else:
                c = arbre.root()
                descr = '\t"N({:s})" [label="{:s}"];\n'.format(prefix, escape_str(c))
                s_a_g = arbre.left()
                label_lien, couleur_lien = ('0', BLACK) if not s_a_g.is_empty() else ('', background_color)
                descr = (descr +
                         aux(s_a_g, prefix+'0') +
                         LIEN.format(prefix, prefix+'0', couleur_lien, label_lien))
                s_a_d = arbre.right()
                label_lien, couleur_lien = ('1', BLACK) if not s_a_d.is_empty() else ('', background_color)
                descr = (descr +
                         aux(s_a_d, prefix+'1') +
                         LIEN.format(prefix, prefix+'1', couleur_lien, label_lien))

            return descr

        return '''/*
  Binary Tree

  Date: {}

*/

digraph G {{
\tbgcolor="{:s}";

{:s}
}}
'''.format(time.strftime('%c'), background_color, aux(self))       

    def show(self, filename='arbre', background_color=WHITE):
        '''
        visualise l'arbre et produit deux fichiers : filename et filename.png
        le premier contenant la description de l'arbre au format dot, 
        le second contenant l'image au format PNG.
        '''
        graphviz.Source(self.to_dot(background_color=background_color),
                        format='png').view(filename=filename)

    def savefig(self, filename='arbre', background_color=WHITE):
        '''
        sauvearde l'arbre et produit deux fichiers : filename et filename.png
        le premier contenant la description de l'arbre au format dot, 
        le second contenant l'image au format PNG.
        '''
        graphviz.Source(self.to_dot(background_color=background_color),
                        format='png').render(filename=filename)
        return f'{filename}.png'


def leaf(n: Node)->Tree:
    """
    :param n: (Node) a node
    :return: (Tree) a leaf
    """
    return Tree(n, Tree(), Tree())

def decision(dt : Tree, datas : dict) -> str:
    """
    :param dt: (Tree) un arbre de décision
    :param datas: (dict) des donnée
    :CU: dt est un arbre de décision 
    """
    n = dt
    while not n.is_leaf() and not n.is_empty():
        crit = n.root().criterion()
        if crit.accept(datas):
            n = n.right()
        else:
            n = n.left()
    if n.is_leaf():
        return str(n.root())
    else:
        return ""

if __name__ == '__main__':
   import doctest
   doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
