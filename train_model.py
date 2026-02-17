import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# ===== ABSOLUTE DATASET PATH (FINAL FIX) =====
csv_path = r"C:\Users\lokeswari\OneDrive\Desktop\Online payments fraud detection\data\PS_20174392719_1491204439457_log.csv"

print("Loading dataset from:", csv_path)

df = pd.read_csv(csv_path)
print("Dataset loaded successfully")

# Preprocessing
df.drop(['nameOrig', 'nameDest'], axis=1, inplace=True)
df = pd.get_dummies(df, columns=['type'], drop_first=True)

X = df.drop('isFraud', axis=1)
y = df['isFraud']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

joblib.dump(model, r"C:\Users\lokeswari\OneDrive\Desktop\Online payments fraud detection\flask\payments.pkl")
print("Model saved successfully")