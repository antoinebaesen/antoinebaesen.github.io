## Importation des modules

from PIL import Image

## Déclaration des constantes

baseImage = Image.open('Exercice1.jpg')

## Déclaration des fonctions

def filtreSansRouge(pixel):
    """
    Retourne un pixel avec la composante rouge à 0
    @param pixel: le pixel à modifier
    @return: la valeur du pixel modifié
    """
    return (0, pixel[1], pixel[2])

def sauvegarderImage(image, nomFichier):
    """Sauvegarde l'image dans un fichier"""
    image.save(nomFichier)

def appliquerFiltre(image, filtre):
    """Applique un filtre à une image"""
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x,y), filtre(image.getpixel((x,y))))

## Fonction principale

def main():
    """Fonction principale"""
    appliquerFiltre(baseImage, filtreSansRouge)
    baseImage.show()
    sauvegarderImage(baseImage, 'Exercice1_rouge.jpg')

## Programme principal

if __name__ == '__main__':
    main()