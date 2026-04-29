# **🏠HPred — Prédiction des Prix Immobiliers**



##### Application desktop développée en Python permettant d’estimer le prix d’un bien immobilier à l’aide des modèles de Machine Learning.

## **📌 Description**



##### HPred est une application avec interface graphique moderne qui permet à l’utilisateur de :

##### 

* ##### Saisir les caractéristiques d’un bien immobilier
* ##### Choisir entre deux modèles de prédiction :

  * ###### ⚡ Modèle rapide (faible latence)
  * ###### 🎯 Modèle précis (meilleure performance)
* ##### Obtenir une estimation instantanée du prix



## **🚀 Fonctionnalités**



##### ✔ Interface graphique moderne avec Tkinter

##### ✔ Champs personnalisés (inputs stylisés)

##### ✔ Toggle switches interactifs

##### ✔ Sélection du modèle (Rapide / Précis)

##### ✔ Affichage dynamique des résultats

##### ✔ Gestion des erreurs utilisateur

##### ✔ Icônes personnalisées (sans emojis)

##### ✔ Design responsive (scroll + adaptatif)



## **🧠 Modèles de Machine Learning**



| Modèle            | Description             | Avantages       |

| ----------------- | ----------------------- | --------------- |

| Linear Regression | Modèle simple et rapide | Très rapide     |

| Gradient Boosting | Modèle avancé           | Haute précision |





## **🖥️ Interface**



##### L’application est divisée en deux parties :

##### 

##### 🔹 Partie gauche

* ##### *Saisie des caractéristiques :*

###### Surface

###### Chambres

###### Salles de bain

###### Étages

###### Parking

* ##### *Options :*

###### Climatisation

###### Sous-sol

###### Zone préférentielle

###### Choix du modèle



##### 🔹 Partie droite

##### Résultat de la prédiction

##### Prix estimé

##### Prix/m²

##### Informations du modèle utilisé





## **📦 Dépendances principales**



* ##### Python 3.x
* ##### Tkinter(GUI)
* ##### NumPy
* ##### Joblib
* ##### Pandas
* ##### scikit-learn



## **⚠️ Gestion des erreurs**



* ##### L’application vérifie :

##### 

###### Les champs vides

###### Les valeurs invalides

###### Les erreurs de prédiction

##### 

##### *Les messages d’erreur sont affichés directement dans l’interface.*



## **📈 Améliorations futures**



* ##### Ajout de graphiques
* ##### Version web (Flask / Django)
* ##### Sauvegarde des prédictions



## **📄 Licence**

##### 

##### Ce projet est destiné à un usage pédagogique.



## **📂 Structure du projet**



HPred/

│

├── app\_desktop/                       # Application bureau Tkinter

│   │

│   ├── app/

│   │   ├── main.py                   # Lancement interface graphique

│   │   ├── \_\_init\_\_.py

│   │   │

│   │   └── assets/                   # Images / icônes interface

│   │       ├── home.png

│   │       ├── money.png

│   │       ├── success.png

│   │       ├── error.png

│   │       └── ...

│   │

│   ├── src/

│   │   ├── predictor.py              # Classe prédiction ML

│   │   └── \_\_init\_\_.py

│   │

│   ├── models/                       # Modèles utilisés par l'app

│   │   ├── fast\_model.pkl

│   │   └── gradient\_boosting\_model.pkl

│   │

│   └── requirements.txt             # Dépendances app desktop

│

├── notebooks/                        # Entraînement / expérimentation

│   ├── FAST\_MODEL.ipynb

│   └── GradientBoosting.ipynb

│

├── data/                             # Jeux de données

│   ├── Housing.csv

│   └── clean\_housing.csv

│

├── docs/                             # Documentation projet

│   └── Cahier\_des\_Charges\_Application\_ML\_Immobilier.pdf

│

├── models/                           # Modèles globaux sauvegardés

│   ├── fast\_model.pkl

│   └── gradient\_boosting\_model.pkl

│

├── .gitignore

├── README.md

└── requirements.txt





















