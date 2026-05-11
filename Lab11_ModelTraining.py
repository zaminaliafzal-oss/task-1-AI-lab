# ============================================================
# Lab 11 Task: Train/Test Split, Model Training & Evaluation
# ============================================================
# Continues from Lab 10 (uses same titanic.csv)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# ── Data Loading & Preprocessing ─────────────────────────────
data = pd.read_csv('titanic.csv')
cols_to_drop = ['PassengerId', 'Name', 'Ticket', 'Cabin']
data.drop(columns=[c for c in cols_to_drop if c in data.columns], inplace=True)
for col in data.columns:
    if data[col].isnull().sum() > 0:
        data[col] = data[col].fillna(data[col].mode()[0])

# ── 1. Split into X and Y ─────────────────────────────────────
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

# ── 2. Encode categorical columns ─────────────────────────────
cat_columns = x.select_dtypes(['object']).columns
x[cat_columns] = x[cat_columns].apply(lambda col: pd.factorize(col)[0])

# ── 3. Train/Test Split ───────────────────────────────────────
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, shuffle=False)

print("=" * 55)
print("      MODEL TRAINING, TESTING & EVALUATION")
print("=" * 55)
print(f"Train size: {X_train.shape[0]}  |  Test size: {X_test.shape[0]}")

# ── Helper function ───────────────────────────────────────────
def evaluate(name, model, X_train, Y_train, X_test, Y_test):
    model.fit(X_train, Y_train)
    preds = model.predict(X_test)
    acc  = accuracy_score(Y_test, preds)
    prec = metrics.precision_score(Y_test, preds, average='weighted', labels=np.unique(preds))
    rec  = metrics.recall_score(Y_test, preds, average='weighted', labels=np.unique(preds))
    f1   = metrics.f1_score(Y_test, preds, average='weighted', labels=np.unique(preds))
    print(f"\n  [{name}]")
    print(f"    Accuracy  : {acc:.4f}")
    print(f"    Precision : {prec:.4f}")
    print(f"    Recall    : {rec:.4f}")
    print(f"    F1 Score  : {f1:.4f}")
    return acc, prec, rec, f1

# ── 4. Apply All Classifiers ──────────────────────────────────
classifiers = {
    'Bernoulli'     : BernoulliNB(),
    'Random Forest' : RandomForestClassifier(random_state=42),
    'Gaussian'      : GaussianNB(),
    'Decision Tree' : DecisionTreeClassifier(random_state=42),
    'Multinomial'   : MultinomialNB(),
    'KNeighbors'    : KNeighborsClassifier(),
}

results = {}
for name, model in classifiers.items():
    results[name] = evaluate(name, model, X_train, Y_train, X_test, Y_test)

labels     = list(results.keys())
accuracies = [results[k][0] for k in labels]
precisions = [results[k][1] for k in labels]
recalls    = [results[k][2] for k in labels]
f1_scores  = [results[k][3] for k in labels]

# ── 5. Line Graph ─────────────────────────────────────────────
plt.figure(figsize=(14, 6))
plt.plot(labels, accuracies,  marker='o', label='Accuracy')
plt.plot(labels, precisions,  marker='o', label='Precision')
plt.plot(labels, recalls,     marker='o', label='Recall')
plt.plot(labels, f1_scores,   marker='o', label='F1 Score')
plt.title("Scores of Applied Classifiers (Line Graph)")
plt.xlabel("Classifiers")
plt.ylabel("Score")
plt.ylim(0, 1.1)
plt.legend()
plt.tight_layout()
plt.savefig('lab11_line_graph.png', dpi=150)
plt.show()
print("\n[Line Graph saved as lab11_line_graph.png]")

# ── 6. Bar Graph ──────────────────────────────────────────────
plt.figure(figsize=(14, 6))
left   = range(1, len(labels) + 1)
colors = ['#08737f', '#00898a', '#089f8f', '#39b48e', '#64c987', '#92dc7e']
plt.bar(left, f1_scores, tick_label=labels, width=0.6, color=colors)
plt.xlabel("Classifiers")
plt.ylabel("F1 Score")
plt.title("F1 Scores of Applied Classifiers (Bar Graph)")
plt.ylim(0, 1.1)
plt.tight_layout()
plt.savefig('lab11_bar_graph.png', dpi=150)
plt.show()
print("[Bar Graph saved as lab11_bar_graph.png]")

print("\n" + "=" * 55)
print("           Evaluation Complete!")
print("=" * 55)
