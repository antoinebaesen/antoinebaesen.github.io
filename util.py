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

"""
for path in paths:
    explore(path)

"""

def replaceAllFileNameByAnother(path : str, toReplace : str, newName : str):
    print(path)
    for directory in os.listdir(path):
        if(os.path.isdir(path + "/" + directory)):
            replaceAllFileNameByAnother(path + "/" + directory, toReplace, newName)
        else:
            if (path + "/" + directory).find(toReplace) != -1:
                os.rename(path + "/" + directory, path + "/" + newName)

"""
for path in paths:
    replaceAllFileNameByAnother(path, "Activite.md", "Manuel.md")
"""

def setStringAtTheStartOfAllFiles(path : str, string : str, target : str):
    print(path)
    for directory in os.listdir(path):
        if(os.path.isdir(path + "/" + directory)):
            setStringAtTheStartOfAllFiles(path + "/" + directory, string, target)
        else:
            if (path + "/" + directory).find(target) != -1:
                with open(path + "/" + directory, "r+") as file:
                    content = file.read()
                    file.seek(0, 0)
                    file.write(string + content)

content = "# Cours \n\
\n\
| [Accueil](..) | [Cours](Cours.md) | [Exercices](Exercices.md) | [Manuel](Manuel.md) | \n\
|:-------:|:-----:|:---------:|:------:| \n\
\n\
"

"""
for path in paths:
    setStringAtTheStartOfAllFiles(path, content, "TestX.md")
"""

# Pour chacunes des images de Src/Images, on va sauvegarder l'image + _32, _64, _128, _256 selon la taille resizer

import os
from PIL import Image

def resizeImage(path : str, size : int):
    for directory in os.listdir(path):
        if(os.path.isdir(path + "/" + directory)):
            resizeImage(path + "/" + directory, size)
        else:
            if (path + "/" + directory).find(".png") != -1:
                if(path + "/" + directory).count("_") == 0 and not os.path.exists(path + "/" + directory[:-4] + "_" + str(size) + ".png"):
                    image = Image.open(path + "/" + directory)
                    image = image.resize((size, size))
                    image.save(path + "/" + directory[:-4] + "_" + str(size) + ".png")
            
resizeImage("Src/Images", 32)
resizeImage("Src/Images", 64)
resizeImage("Src/Images", 128)
resizeImage("Src/Images", 256)
"""
"""

# Pour chacunes des images de Src/Images, on delete les images contenant au moins 2 '_'

def deleteImage(path : str):
    for directory in os.listdir(path):
        if(os.path.isdir(path + "/" + directory)):
            deleteImage(path + "/" + directory)
        else:
            # Si le fichier contient au moins 2 '_'
            if (path + "/" + directory).count("_") > 1:
                os.remove(path + "/" + directory)

"""
deleteImage("Src/Images")
"""
