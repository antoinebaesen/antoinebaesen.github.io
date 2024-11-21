# On importe les modules pour créer un exemple de classification par Bayes naïf

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# On charge ici le jeu de données
iris = datasets.load_iris()

# On divise ici le jeu de données en deux parties : une pour l'entraînement et une pour les tests
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# On crée ici un modèle de Bayes naïf
model = GaussianNB()

# On entraîne ici le modèle
model.fit(X_train, y_train)

# On évalue ici le modèle
model.score(X_test, y_test)

# On affiche ici les prédictions
predictions = model.predict(X_test)

for i in range(10):
    print(f"La prédiction est {predictions[i]}")
    print(f"La vraie valeur est {y_test[i]}")

# On affiche ici les scores du modèle
print(f"Le score du modèle est {model.score(X_test, y_test) * 100} %")
# On affiche ici les moyennes des variables pour chaque classe
print(f"Les moyennes des variables pour chaque classe sont {model.theta_}")
