import os
import joblib
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, classification_report


TRAIN_CSV = "Training.csv"
TEST_CSV = "Testing.csv"
MODEL_OUT = "rf_disease_model.pkl"
ENCODER_OUT = "disease_label_encoder.pkl"
COLS_OUT = "symptom_columns.pkl"
RANDOM_STATE = 42


train_df = pd.read_csv(TRAIN_CSV)
label_col = "prognosis"

X = train_df.drop(columns=[label_col])
y = train_df[label_col]


le = LabelEncoder()
y_enc = le.fit_transform(y)


rf = RandomForestClassifier(
    n_estimators=600,         
    max_depth=25,             
    min_samples_split=2,
    min_samples_leaf=1,
    class_weight="balanced",  
    random_state=RANDOM_STATE,
    n_jobs=-1
)


cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
cv_scores = cross_val_score(
    rf, X, y_enc,
    cv=cv,
    scoring="accuracy",
    n_jobs=-1
)

print("CV Accuracy scores:", cv_scores)
print("Mean CV Accuracy:", cv_scores.mean())


rf.fit(X, y_enc)


joblib.dump(rf, MODEL_OUT)
joblib.dump(le, ENCODER_OUT)
joblib.dump(X.columns.tolist(), COLS_OUT)

print("✅ Model, encoder & columns saved")


if os.path.exists(TEST_CSV):
    test_df = pd.read_csv(TEST_CSV)
    X_test = test_df.drop(columns=[label_col])
    y_test = le.transform(test_df[label_col])

    y_pred = rf.predict(X_test)
    print("\nTest Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred, target_names=le.classes_))

