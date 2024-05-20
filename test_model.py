import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from model_creation import X_train, X_test, y_test, params
from sklearn import metrics
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import mlflow
from mlflow.models import infer_signature

# load
with open('data/model_knn/neigh_model.pkl', 'rb') as f:
    neigh_model = pickle.load(f)
y_pred = neigh_model.predict(X_test)
model_accuracy = accuracy_score(y_test, y_pred)     
print(confusion_matrix(y_test, y_pred)) 
print(classification_report(y_test, y_pred))

# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri="http://127.0.0.1:5005")

# Create a new MLflow Experiment
mlflow.set_experiment("MLflow Quickstart")

# Start an MLflow run
with mlflow.start_run():
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log the loss metric
    mlflow.log_metric("accuracy", model_accuracy)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Basic knn model for cancer breast data")

    # Infer the model signature
    signature = infer_signature(X_train, neigh_model.predict(X_train))

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=neigh_model,
        artifact_path="cancer_breast_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="tracking-quickstart",
    )
    
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)

predictions = loaded_model.predict(X_test)

