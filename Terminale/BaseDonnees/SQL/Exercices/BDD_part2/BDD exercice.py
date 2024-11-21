# Créé par JP, le 05/10/2022 en Python 3.7



import sqlite3

bdd = sqlite3.connect("bdd.db")
# les tables seront stockées dans le fichier en paramètre
curseur = bdd.cursor()
# obligatoire

def creation():
    requete ="""
    CREATE TABLE exemple
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        nom TEXT,
        nombre INTEGER
    );
    """
    curseur.execute(requete) # obligatoire pour exécuter la requête
    bdd.commit() # obligatoire , le fichier est créé

def donnees(a:int,b:str,c:int):
    curseur.execute("INSERT INTO exemple VALUES ("+str(a)+",'"+b+"',"+str(c)+");")
    # On ajoute deux enregistrements dans la table exemple
    bdd.commit()
    # obligatoire , le fichier est modifié



def lecture():
    requete = " SELECT * FROM exemple"
    curseur.execute(requete)
    # obligatoire pour exécuter la requête
    for element in curseur :
        print(element)
        # permet d'afficher tous les enregistrements


#bdd.close() #Déconnexion # obligatoire
