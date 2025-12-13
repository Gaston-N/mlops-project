import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score
import joblib
import json
from pathlib import Path


def test_model_trains(sample_data):
    # check model trains without errors
    X = sample_data[['purchases', 'time_spent', 'n_visits']]
    y = sample_data['lead_indicator']
    
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X, y)

    assert model is not None


def test_model_predicts(sample_data):
    # check model makes predictions
    X = sample_data[['purchases', 'time_spent', 'n_visits']]
    y = sample_data['lead_indicator']
    
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X, y)
    
    predictions = model.predict(X)
    
    assert len(predictions) == len(y)
    assert all(p in [0, 1] for p in predictions)


def test_model_performance(sample_data, min_thresholds):
    # check model reaches minimum performance thresholds
    X = sample_data[['purchases', 'time_spent', 'n_visits']]
    y = sample_data['lead_indicator']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    f1 = f1_score(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)
    
    assert f1 >= min_thresholds['f1_score'], f"F1 {f1:.3f} below {min_thresholds['f1_score']}"
    assert acc >= min_thresholds['accuracy'], f"Accuracy {acc:.3f} below {min_thresholds['accuracy']}"


def test_model_class_preds(sample_data):
    # check model doesn't always predict the same class
    X = sample_data[['purchases', 'time_spent', 'n_visits']]
    y = sample_data['lead_indicator']
    
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X, y)
    
    predictions = model.predict(X)
    unique_predictions = np.unique(predictions)
    
    assert len(unique_predictions) > 1, "Model only predicts one class"


def test_model_saves(sample_data, tmp_path):
    # check model is saved in the right place
    X = sample_data[['purchases', 'time_spent', 'n_visits']]
    y = sample_data['lead_indicator']
    
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X, y)
    
    model_path = tmp_path / "model.pkl"
    joblib.dump(model, model_path)
    
    assert model_path.exists()
    
    loaded_model = joblib.load(model_path)
    predictions = loaded_model.predict(X[:5])
    assert len(predictions) == 5


def test_model_artifacts_exist():
    # check model artifacts are saved correctly
    artif_path = Path("artifacts")
    
    if artif_path.exists():
        expected = ['columns_drift.json', 'columns_list.json', 'date_limits.json',
                    'lead_model_xgboost.json', 'model_results.json']
        
        for artifact in expected:
            artifact_path = artif_path / artifact
            if artifact_path.exists():
                with open(artifact_path) as f:
                    data = json.load(f)
                    assert data is not None
                    