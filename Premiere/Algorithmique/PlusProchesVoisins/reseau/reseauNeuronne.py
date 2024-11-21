# On importe ici les modules nécessaires
import numpy as np
import matplotlib.pyplot as plt

# Scikit-learn est une bibliothèque qui contient de nombreux outils pour l'apprentissage automatique
from sklearn import datasets

# On importe ici la fonction train_test_split qui permet de diviser un jeu de données en deux parties
from sklearn.model_selection import train_test_split

# On importe ici le modèle de réseau de neuronne
from sklearn.neural_network import MLPClassifier

# On importe ici la fonction pour afficher les images
from sklearn.datasets import load_digits

# On charge ici le jeu de données
digits = load_digits()

# On divise ici le jeu de données en deux parties : une pour l'entraînement et une pour les tests
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)

# On crée ici un modèle de réseau de neuronne
model = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=400, alpha=0.0001, solver='sgd', verbose=10,  random_state=21,tol=0.000000001)

# On entraîne ici le modèle

"""
L'entrainement suit ce modèle :
- On initialise les poids et les biais aléatoirement
- On calcule la sortie du réseau
- On compare la sortie du réseau avec la sortie attendue
- On ajuste les poids et les biais pour minimiser l'erreur entre la sortie du réseau et la sortie attendue en fonction de la fonction de coût
- On répète les étapes 2 à 4 jusqu'à ce que l'erreur soit suffisamment faible
"""

model.fit(X_train, y_train)

# On évalue ici le modèle
model.score(X_test, y_test)

# On affiche ici les prédictions
predictions = model.predict(X_test)

for i in range(10):
    plt.matshow(digits.images[i])
    plt.show()
    print(f"La prédiction est {predictions[i]}")
    print(f"La vraie valeur est {y_test[i]}")

# On affiche ici les poids du modèle
print(model.coefs_)

# On affiche ici les biais du modèle
print(model.intercepts_)

# On affiche ici les scores du modèle
print(model.score(X_test, y_test))