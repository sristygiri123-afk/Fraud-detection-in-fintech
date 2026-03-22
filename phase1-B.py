import matplotlib.pyplot as plt
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# ==============================
# LOAD DATA
# ==============================

df = pd.read_csv('creditcard.csv')

# Original distribution
counts_before = df["Class"].value_counts()

# ==============================
# FEATURES & TARGET
# ==============================

X = df.drop('Class', axis=1)
y = df['Class']

# ==============================
# TRAIN-TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ==============================
# APPLY SMOTE (ONLY TRAIN DATA)
# ==============================

smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

counts_after = y_train_smote.value_counts()

# ==============================
# TRAIN MODEL
# ==============================

model = RandomForestClassifier(random_state=42)
model.fit(X_train_smote, y_train_smote)

# ==============================
# EVALUATION
# ==============================

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ==============================
# SAVE MODEL
# ==============================

joblib.dump(model, "fraud_detection_model_smote.pkl")
print("\nModel saved successfully!")

# ==============================
# PLOT GRAPHS
# ==============================

plt.figure(figsize=(10,4))

# Before SMOTE
plt.subplot(1,2,1)
plt.bar(["Legitimate","Fraud"], counts_before.values)
plt.title("Before SMOTE")
plt.xlabel("Transaction Type")
plt.ylabel("Count")

# After SMOTE (training data)
plt.subplot(1,2,2)
plt.bar(["Legitimate","Fraud"], counts_after.values)
plt.title("After SMOTE (Training Data)")
plt.xlabel("Transaction Type")

plt.tight_layout()
plt.show()