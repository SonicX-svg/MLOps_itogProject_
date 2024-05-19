# Загрузка необходимых библиотек
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
import os

# Загрузка данных
df_train = pd.read_csv('MLOps_itogProject_/data/model/train.csv')

y = df_train[['target']]
X = df_train.drop('target', axis=1)

# размер тестовой выборки составит 30%
# также зададим точку отсчета для воспроизводимости результата
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.3, 
                                                    random_state = 42)


neigh = LogisticRegression(random_state=0)
neigh.fit(X_train, y_train.values.ravel())


try:
    if os.path.exists('MLOps_itogProject_/data/model_knn') is True:
        with open('MLOps_itogProject_/data/model_knn/neigh_model.pkl', 'wb') as f:
            pickle.dump(neigh, f)
            print('Модель сохранена', '\n')
    else:
        os.mkdir('MLOps_itogProject_/data/model_knn')
        with open('MLOps_itogProject_/data/model_knn/neigh_model.pkl', 'wb') as f:
            pickle.dump(neigh, f)
except:
    print('Не удалось сохранить модель', '\n')
