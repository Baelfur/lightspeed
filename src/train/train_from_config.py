# src/train/train_from_config.py

import pandas as pd
import json
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_from_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)

    df = pd.read_csv(config["input_csv"])
    X = df[config["features"]]
    y = df[config["label"]]
    X = X.fillna("missing")
    X = pd.get_dummies(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.get("test_size", 0.2), 
        random_state=config.get("random_state", 42), stratify=y
    )

    # Build model params from config
    rf_params = {}
    if "model_params" in config:
        rf_params = config["model_params"]
    else:
        # Legacy support for n_estimators etc at top-level
        for k in ["n_estimators", "max_depth", "min_samples_split", "min_samples_leaf"]:
            if k in config:
                rf_params[k] = config[k]

    clf = RandomForestClassifier(**rf_params)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("--- Model Report ---")
    print(classification_report(y_test, y_pred))

    # Save classification report as JSON if specified
    output_report = config.get("output_report", None)
    if output_report:
        os.makedirs(os.path.dirname(output_report), exist_ok=True)
        report_dict = classification_report(y_test, y_pred, output_dict=True)
        with open(output_report, "w") as f:
            json.dump(report_dict, f, indent=2)

    # Save model and encoder
    model_output = config.get("output_model", "models/model.joblib")
    encoder_output = config.get("output_encoder", "models/encoder.joblib")
    os.makedirs(os.path.dirname(model_output), exist_ok=True)
    os.makedirs(os.path.dirname(encoder_output), exist_ok=True)
    joblib.dump(clf, model_output)
    joblib.dump(X.columns, encoder_output)

    # Save feature importance plot if specified
    output_plot = config.get("output_plot", None)
    if output_plot:
        os.makedirs(os.path.dirname(output_plot), exist_ok=True)
        import matplotlib.pyplot as plt
        importances = clf.feature_importances_
        indices = importances.argsort()[::-1]
        top_n = config.get("top_n_features", 20)
        plt.figure(figsize=(10, 6))
        plt.title("Feature Importances")
        plt.bar(range(min(top_n, len(indices))), importances[indices[:top_n]])
        plt.xticks(range(min(top_n, len(indices))), X.columns[indices[:top_n]], rotation=90)
        plt.tight_layout()
        plt.savefig(output_plot)
        plt.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    train_from_config(args.config)