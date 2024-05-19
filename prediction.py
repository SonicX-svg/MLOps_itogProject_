from model_creation import X_test, y_test
import pickle
from sklearn.metrics import classification_report, confusion_matrix
import os

# load
try:
    if os.path.exists('MLOps_itogProject_/data/model_knn') is True:
        with open('MLOps_itogProject_/data/model_knn/neigh_model.pkl', 'rb') as f:
            neigh_model = pickle.load(f)
    else:
        os.mkdir('MLOps_itogProject_/data/model_knn')
except:
    print('файл не существует')

y_pred = neigh_model.predict(X_test)

#Print the Confusion Matrix and slice it into four pieces
print("Confusion matrix: \n",confusion_matrix(y_test, y_pred))

#Print a classification report.
print("Classification report: \n", classification_report(y_test, y_pred))
