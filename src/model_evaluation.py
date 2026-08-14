import json
import pickle

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

# Charger le modèle
with open("model.pkl", "rb") as f:
    clf = pickle.load(f)

# Charger les données de test
test_data = pd.read_csv("./data/features/test_bow.csv")

# Séparer les variables et la cible
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values

# Effectuer les prédictions
y_pred = clf.predict(X_test)

# Vérifier si le modèle supporte predict_proba
if hasattr(clf, "predict_proba"):
    y_pred_proba = clf.predict_proba(X_test)

    # Trouver l'indice de la classe "happiness"
    positive_class = "happiness"
    class_index = list(clf.classes_).index(positive_class)

    auc = roc_auc_score(
        y_test,
        y_pred_proba[:, class_index],
        labels=clf.classes_
    )
else:
    auc = None

# Calcul des métriques
metrics_dict = {
    "accuracy": accuracy_score(y_test, y_pred),
    "precision": precision_score(
        y_test,
        y_pred,
        pos_label="happiness",
        zero_division=0,
    ),
    "recall": recall_score(
        y_test,
        y_pred,
        pos_label="happiness",
        zero_division=0,
    ),
    "auc": auc,
}

# Afficher les résultats
print("\n===== Résultats =====")
for key, value in metrics_dict.items():
    print(f"{key}: {value}")

# Sauvegarder les métriques
with open("metrics.json", "w") as f:
    json.dump(metrics_dict, f, indent=4)

print("\nLes métriques ont été enregistrées dans metrics.json")