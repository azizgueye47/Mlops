# 🧠 MLOps — Analyse de sentiment

## 📌 Description du projet

Ce projet met en place une **pipeline MLOps complète pour l'analyse automatique de sentiment de textes**.

L'objectif est de développer un modèle capable de classifier automatiquement des commentaires ou messages selon leur sentiment, par exemple :

* 😊 **Positif**
* 😐 **Neutre**
* 😠 **Négatif**

Au-delà de la construction du modèle de Machine Learning, le projet cherche à mettre en œuvre une démarche **MLOps** permettant de rendre le pipeline reproductible, versionné, maintenable et facilement déployable.

Le projet couvre ainsi les différentes étapes du cycle de vie d'un modèle :

```text
Collecte des données
        ↓
Préparation / Nettoyage
        ↓
Exploration des données
        ↓
Prétraitement du texte
        ↓
Entraînement du modèle
        ↓
Évaluation
        ↓
Versionnement des données et du code
        ↓
Reproductibilité du pipeline
        ↓
Déploiement
```

---

## 🎯 Objectifs

Les principaux objectifs du projet sont :

* développer un modèle de classification de sentiment ;
* automatiser les différentes étapes du pipeline Machine Learning ;
* versionner les données et les modèles ;
* assurer la reproductibilité des expériences ;
* organiser le projet selon une architecture MLOps ;
* suivre les différentes étapes du pipeline avec **DVC** ;
* utiliser **Git/GitHub** pour le versionnement du code ;
* préparer le modèle pour une future mise en production.

---

## 🏗️ Architecture du projet

Le projet est organisé de la manière suivante :

```text
Mlops/
│
├── .dvc/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── ...
│
├── notebook/
│   └── ...
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── ...
│
├── MLops/
│   └── ...
│
├── .dvcignore
├── .gitignore
├── dvc.yaml
├── dvc.lock
├── requirements.txt
└── README.md
```

### 📂 Description des dossiers

| Dossier / fichier  | Description                                    |
| ------------------ | ---------------------------------------------- |
| `.dvc/`            | Configuration et métadonnées de DVC            |
| `data/`            | Données utilisées par le projet                |
| `notebook/`        | Exploration des données et expérimentations    |
| `src/`             | Code source du pipeline                        |
| `MLops/`           | Éléments liés à l'organisation du projet MLOps |
| `dvc.yaml`         | Définition des étapes du pipeline DVC          |
| `dvc.lock`         | Versions et dépendances exactes du pipeline    |
| `requirements.txt` | Dépendances Python                             |
| `.gitignore`       | Fichiers exclus du versionnement Git           |
| `.dvcignore`       | Fichiers exclus du suivi DVC                   |

---

## 🔄 Pipeline Machine Learning

Le pipeline est structuré en plusieurs étapes.

### 1. 📥 Préparation des données

Les données textuelles sont chargées puis nettoyées afin de préparer les commentaires pour le modèle.

Les opérations peuvent notamment inclure :

* suppression des valeurs manquantes ;
* nettoyage du texte ;
* normalisation ;
* suppression des caractères inutiles ;
* préparation des variables d'entrée et de la variable cible.

### 2. 🔎 Analyse exploratoire

Une analyse exploratoire permet de comprendre :

* la distribution des classes ;
* la fréquence des mots ;
* la longueur des commentaires ;
* les éventuels déséquilibres entre les classes.

### 3. 🧹 Prétraitement du texte

Les textes sont transformés en représentations numériques exploitables par les algorithmes de Machine Learning.

Selon l'approche retenue, cela peut utiliser :

* TF-IDF ;
* Bag of Words ;
* embeddings ;
* modèles pré-entraînés de NLP.

### 4. 🤖 Entraînement

Le modèle est entraîné sur les données préparées.

Le projet peut comparer plusieurs algorithmes afin d'identifier le modèle offrant les meilleures performances.

### 5. 📊 Évaluation

Les performances du modèle sont évaluées à l'aide de métriques adaptées à la classification :

* Accuracy ;
* Precision ;
* Recall ;
* F1-score ;
* Matrice de confusion.

---

# ⚙️ Approche MLOps

L'objectif principal du projet est de ne pas considérer le modèle uniquement comme un notebook, mais comme **un pipeline reproductible**.

## 🔹 Git & GitHub

Git est utilisé pour versionner :

* le code source ;
* les notebooks ;
* les fichiers de configuration ;
* les modifications du pipeline.

GitHub permet également de collaborer et de conserver l'historique du projet.

## 🔹 DVC

**DVC (Data Version Control)** est utilisé pour gérer les données et automatiser le pipeline Machine Learning.

Les étapes du pipeline sont définies dans :

```text
dvc.yaml
```

Les versions et dépendances générées par DVC sont enregistrées dans :

```text
dvc.lock
```

Le pipeline peut ainsi être reproduit avec :

```bash
dvc repro
```

Le graphe des différentes étapes peut être visualisé avec :

```bash
dvc dag
```

Cette approche permet de suivre les dépendances entre les différentes étapes du projet et de reproduire les résultats à partir d'un état donné du projet.

---

# 🚀 Installation

## 1. Cloner le repository

```bash
git clone https://github.com/azizgueye47/Mlops.git
cd Mlops
```

## 2. Créer un environnement virtuel

```bash
python -m venv env
```

### Windows

```bash
env\Scripts\activate
```

### Linux / WSL

```bash
source env/bin/activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# ▶️ Exécution du pipeline

Une fois l'environnement configuré :

```bash
dvc repro
```

Pour visualiser le pipeline :

```bash
dvc dag
```

Pour vérifier l'état du projet :

```bash
dvc status
```

---

# 📈 Résultats

Le projet permet d'obtenir un modèle capable de prédire automatiquement le sentiment associé à un texte.

Exemple :

```text
Entrée :
"Le service est excellent et très rapide !"

Prédiction :
😊 Positif
```

```text
Entrée :
"Le produit est vraiment décevant."

Prédiction :
😠 Négatif
```

L'objectif à terme est de transformer ce modèle en un service exploitable dans une application réelle.

---

# 🔮 Perspectives

Plusieurs améliorations peuvent être ajoutées au projet :

* [ ] Ajouter MLflow pour le suivi des expériences ;
* [ ] Ajouter une API avec FastAPI ;
* [ ] Conteneuriser l'application avec Docker ;
* [ ] Mettre en place une CI/CD avec GitHub Actions ;
* [ ] Ajouter un monitoring du modèle ;
* [ ] Ajouter un système de détection de dérive des données ;
* [ ] Déployer le modèle sur le cloud ;
* [ ] Ajouter une interface utilisateur avec Streamlit ;
* [ ] Tester des modèles NLP plus avancés ;
* [ ] Automatiser le réentraînement du modèle.

---

# 🛠️ Technologies utilisées

| Technologie       | Utilisation                            |
| ----------------- | -------------------------------------- |
| 🐍 Python         | Développement                          |
| 🐼 Pandas         | Manipulation des données               |
| 🔢 NumPy          | Calcul numérique                       |
| 🤖 Scikit-learn   | Machine Learning                       |
| 📓 Jupyter        | Expérimentation                        |
| 🌳 Git            | Versionnement du code                  |
| 🐙 GitHub         | Collaboration et hébergement           |
| 📦 DVC            | Versionnement des données et pipelines |
| 🐳 Docker         | Conteneurisation — prévu               |
| 📊 MLflow         | Tracking des expériences — prévu       |
| ⚡ FastAPI         | API — prévu                            |
| 🔄 GitHub Actions | CI/CD — prévu                          |

---

# 🧩 Architecture MLOps cible

L'évolution du projet peut suivre l'architecture suivante :

```text
                    ┌──────────────┐
                    │   GitHub     │
                    │ Code + CI/CD │
                    └──────┬───────┘
                           │
                           ▼
┌────────────┐      ┌──────────────┐
│    Data    │ ───► │     DVC      │
└────────────┘      └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ ML Pipeline  │
                    │              │
                    │ Preprocessing│
                    │ Training     │
                    │ Evaluation   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   MLflow     │
                    │ Experiments  │
                    │ Models       │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Docker    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  FastAPI     │
                    │ Model API    │
                    └──────────────┘
```

---

# 👨‍💻 Auteur

**Abdoul Aziz Gueye**

Data Analyst / BI & Machine Learning / MLOps

GitHub : `azizgueye47`

---

## 📄 Licence

Ce projet est distribué sous licence MIT.
