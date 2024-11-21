import sys
from tree import Tree, TreeError, Node, BooleanTreeNode, TestNode, leaf, decision
from criterion import LessThanCriterion, EqualCriterion, GreaterThanCriterion
from entropy import *
from classification_common import regroupe
sys.path.append('src')
from classification_common import read_example_file

examples : list[dict] = read_example_file('choixpeauMagique.csv')

def a_la_meme_classe(examples : list[dict]) -> bool:
     """
     Fonction qui permet de savoir si tous les exemples ont la meme classe
     
     Parametres :
          examples : (dict) exemples a tester
          
     Retour :
          (bool) True si tous les exemples ont la meme classe, False sinon
     """
     res : bool = True
     i : int = 0
     while i < len(examples)-1 and res:
          if examples[i]['Maison'] != examples[i+1]['Maison']:
               res = False
          i += 1
     return res

def creer_arbre(donnees : list[dict], attributs : list[str]) -> dict:
     print(f"donnees : {donnees}, attributs : {attributs}")
     # Si toutes les donnees ont la meme classe, ou si attributs est vide, alors on renvoie la classe la plus frequente
     if (attributs == [] or a_la_meme_classe(donnees)):
          if(len(donnees) == 0):
               return leaf('Aucune maison')

          return leaf(donnees[0]['Maison'])
     
     # Sinon, on choisit le meilleur attribut pour diviser les donnees
     else:
          # On initialise la meilleure entropie a l'infini
          meilleurGain = 0
          meilleurCouple : tuple[str, int] = (None, 0)
          entropieValeurExacte : bool = True

          # On parcourt les attributs
          for attribut in attributs:
               dictionnaire = regroupe(donnees, attribut)
               gainActuel = gain(donnees, dictionnaire.values(), "Maison")

               for i in range(2, 9):
                    cluster : list[list[dict]] = sum(donnees[k] for k in donnees if k[attribut] <= i)
                    gainActuel = gain(donnees, cluster, "Maison")
                    if gainActuel > meilleurGain:
                         meilleurGain = gainActuel
                         meilleurCouple = (attribut, i)
                         entropieValeurExacte = False

          # On divise les donnees en fonction de l'attribut choisi
          donneesGauche : list[dict] = []
          donneesDroite : list[dict] = []

          print(f"meilleurCouple : {meilleurCouple} {len(donnees)}")

          if(meilleurCouple[0] == None):
               return leaf('Aucune maison')
          
          print(f"je coupe avec {meilleurCouple[0]} et {meilleurCouple[1]} {len(donnees)}")

          for donnee in donnees:
               if(entropieValeurExacte):
                    if donnee[meilleurCouple[0]] == meilleurCouple[1]:
                         donneesGauche.append(donnee)
                    else:
                         donneesDroite.append(donnee)
               else:
                    if donnee[meilleurCouple[0]] <= meilleurCouple[1]:
                         donneesGauche.append(donnee)
                    else:
                         donneesDroite.append(donnee)
          
          print(f"donneesGauche : {len(donneesGauche)}, donneesDroite : {len(donneesDroite)}")

          attributs.remove(meilleurCouple[0])
          g : dict = creer_arbre(donneesGauche, attributs)
          d : dict = creer_arbre(donneesDroite, attributs)

          return decision(meilleurCouple[0], meilleurCouple[1], g, d)
    
arbre = creer_arbre(examples, ['Sagesse', 'Loyaute', 'Courage', 'Malice' ])
repr(arbre)
