import csv

# Ouvre le fichier csv "nat2022.csv" et affiche les données dans un tableau

# Renvoie le nom le plus donné en 2022 et le nombre de fois qu'il a été donné
def plus_donnee(annee : int = 2022):

    nombre_max = 0
    nom_max = ""

"""
    with open('nat2022.csv', newline='', encoding='utf-8') as csvfile:
        # Crée un objet reader
        reader = csv.reader(csvfile, delimiter=';')
        # Pour chaque ligne du fichier
        for row in reader:

            # Si l'année correspond bien à 2022, on passe à la suivante
            if ........... == str(.........) and row[1] != "_PRENOMS_RARES":

                # La 4ème colonne contient le nombre de personnes
                occurrences = int(...........)

                # Si le nombre de personnes est supérieur au nombre maximum
                if occurrences > .............:

                    # Met à jour le nombre maximum et le nom maximum
                    nombre_max = ..............
                    # Le nom est dans la colonne 2
                    nom_max = ..............

        # Affiche le nom le plus donné et le nombre de fois qu'il a été donné
        print(f"Le nom le plus donné en {annee} est {nom_max} avec {nombre_max} occurrences \n\n")
"""

# récupère le nombre de personne total avec un certain nom
def nombre_personne(nom : str):
    nom = nom.upper()
    with open('nat2022.csv', newline='', encoding='utf-8') as csvfile:
        # Crée un objet reader
        reader = csv.reader(csvfile, delimiter=';')
        # Compte le nombre de personnes avec le nom donné
        nombre = 0
        for row in reader:
            if nom in row:
                # La 4ème colonne contient le nombre de personnes
                occurrences = int(row[3])
                nombre += occurrences
        # Affiche le nombre de personnes
        print(f"Il y a {nombre} personnes avec le nom {nom} \n\n")

    # Ferme le fichier csv
    csvfile.close()

# Fonction pour lire les données d'une seule personne
def lire_donnees_personne():
    nom = nom.upper()
    # Demande à l'utilisateur de saisir un nom
    nom = input("Entrez le nom de la personne: ")

    with open('nat2022.csv', newline='', encoding='utf-8') as csvfile:
        # Crée un objet reader
        reader = csv.reader(csvfile, delimiter=';')
        # Pour chaque ligne du fichier
        for row in reader:
            # Si le nom de la personne est dans la ligne
            if nom in row:
                # Affiche la ligne
                print(row)

    # Ferme le fichier csv
    csvfile.close()

# Fonction pour lire toutes les 100 premières données
def lire_donnees():
    with open('nat2022.csv', newline='', encoding='utf-8') as csvfile:
        # Crée un objet reader
        reader = csv.reader(csvfile, delimiter=';')
        # Pour chaque ligne du fichier
        for i, row in enumerate(reader):
            # Si on a affiché 100 lignes, on sort de la boucle
            if i == 100:
                break
            # Affiche la ligne
            print(row)

    # Ferme le fichier csv
    csvfile.close()

# Menu principal

# Affiche le menu
while True:
    print("Menu principal")
    print("1. Afficher les 100 premières données")
    print("2. Afficher les données d'une seule personne")
    print("3. Afficher le nombre de personnes avec un certain nom")
    print("4. Afficher le nom le plus donné")
    print("5. Quitter")

    # Demande à l'utilisateur de choisir une option
    option = int(input("Choisissez une option: "))
    # Verifie que l'entrée ne prend que des nombres
    try:
        option = int(option)
    except ValueError:
        print("Entrez un nombre")
        continue

    if option == 1:
        lire_donnees()
    elif option == 2:
        lire_donnees_personne()
    elif option == 3:
        nom = input("Entrez le nom: ")
        nombre_personne(nom)
    elif option == 4:
        plus_donnee()
    elif option == 5:
        break
    else:
        print("Option invalide")