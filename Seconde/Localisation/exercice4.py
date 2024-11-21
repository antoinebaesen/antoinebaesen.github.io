from PIL import Image

# Ouvrir l'image
img = Image.open("exercice 1.jpg")

# Récupérer les métadonnées sous la forme d'un dictionnaire
metadata = img.info

print(metadata)