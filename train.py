# src/train.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib
import os

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

models = {
    "logreg": LogisticRegression(max_iter=200),
    "tree": DecisionTreeClassifier(random_state=42),
    "svm": SVC()
}
best_acc, best_model_name, best_model = 0, None, None
for name, m in models.items():
    m.fit(X_train, y_train)
    acc = accuracy_score(y_test, m.predict(X_test))
    print(name, acc)
    if acc > best_acc:
        best_acc, best_model_name, best_model = acc, name, m

os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/iris_model.joblib")
print("Saved", best_model_name, "model with acc", best_acc)
