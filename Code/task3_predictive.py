"""
Task 3: Predictive Analytics for Resource Allocation
File: code/task3_predictive.py

This script loads sklearn's breast cancer dataset, constructs a synthetic 3-class "priority"
label for illustration, trains a RandomForest, and outputs metrics and a confusion matrix image.

Run:
    python code/task3_predictive.py
"""

import os
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

OUTPUT_DIR = os.path.join("report", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    # Original label: 0=malignant, 1=benign
    # Build a synthetic risk score to map into {low, medium, high}
    risk_score = X['mean radius'] * 0.6 + X['mean texture'] * 0.4
    risk_score = (risk_score - risk_score.min()) / (risk_score.max() - risk_score.min())

    y_priority = pd.cut(risk_score, bins=[-1, 0.33, 0.66, 1.01], labels=['low', 'medium', 'high']).astype(str)
    label_map = {'low': 0, 'medium': 1, 'high': 2}
    y = y_priority.map(label_map)

    # Handle any NaNs (shouldn't be any)
    X = X.fillna(0)

    # Preprocess
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

    clf = RandomForestClassifier(n_estimators=200, random_state=42, class_weight='balanced')
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1_macro = f1_score(y_test, y_pred, average='macro')

    print("Accuracy:", round(acc, 4))
    print("F1 (macro):", round(f1_macro, 4))
    print("\nClassification report:\n")
    print(classification_report(y_test, y_pred, target_names=['low', 'medium', 'high']))

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['low','medium','high'], yticklabels=['low','medium','high'])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix — Priority Prediction")
    cm_path = os.path.join(OUTPUT_DIR, "confusion_matrix.png")
    plt.tight_layout()
    plt.savefig(cm_path, dpi=150)
    print("Confusion matrix saved to:", cm_path)

    # Save model & scaler for reproducibility
    model_path = os.path.join(OUTPUT_DIR, "rf_priority_model.joblib")
    scaler_path = os.path.join(OUTPUT_DIR, "scaler.joblib")
    joblib.dump(clf, model_path)
    joblib.dump(scaler, scaler_path)
    print("Model saved to:", model_path)

if __name__ == "__main__":
    main()
