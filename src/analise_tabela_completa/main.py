import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

file_path = "best_data.csv"

data = pd.read_csv(file_path, sep=";")


data.columns = data.columns.str.strip()

data["target"] = data[["FALHAS_ROD"]].max(axis=1)

X = data.drop(columns=["KNR", "MOD", "FALHAS_ROD", "TROCA_PECA", "REPINT", "target"])

y = data["target"]
if "MOD" in X.columns:
    le = LabelEncoder()
    X["MOD"] = le.fit_transform(X["MOD"])

X = X.apply(pd.to_numeric, errors="coerce")

X = X.dropna()
y = y.loc[X.index]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# import joblib

# joblib.dump(rf_model, "falhaROD.pkl")
