from PIL import Image

# Ouvrir l'image
img = Image.open("exercice4.png")

# Récupérer les métadonnées sous la forme d'un dictionnaire
metadata = img.info

# Ajoute des métadonnées de localisation sur l'image
metadata["gps_position"] = (50.627557, 3.068958)

# Enregistre l'image avec les nouvelles métadonnées
img.save("exercice4.png", **metadata)

# Affiche les métadonnées
print(metadata)