import os

paths = ["Seconde", "Premiere", "Terminale", "AutresRessources"]
def set(path):
    filesToCreate = ["Cours.md", "Exercices.md", "Corrections.md", "Activite.md"]
    for file in filesToCreate:
        if not os.path.exists(path + "/" + file):
            open(path + "/" + file, "w+").close()
    # Create

# foreach file in the list

def explore(path):
    if not os.path.isdir(path) or path[0] == ".":
        return

    for directory in os.listdir(path):
        if(not os.path.isdir(path + "/" + directory)):
            continue

        # if the directory is empty
        elif len(os.listdir(path + "/" + directory)) == 0:
            print("Empty directory: " + path + "/" + directory)
            set(path + "/" + directory)
        else:
            explore(path + "/" + directory)

for path in paths:
    explore(path)
