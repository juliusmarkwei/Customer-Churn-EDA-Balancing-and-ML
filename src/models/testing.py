import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from lightgbm import LGBMClassifier
from xgboost.sklearn import XGBClassifier



df = pd.read_csv('../data/raw/Customer-Churn-Records.csv', sep = ',')
X = df.drop('Exited', axis = 1)
X = X.values
y = df['Exited']

scaler = StandardScaler()
X_standard = scaler.fit_transform(X)

X_train,X_test, y_train, y_test = train_test_split(X_standard, y, test_size = 0.3, random_state = 0)

# GaussianNB model
naive_bayes = GaussianNB()
previsoes = naive_bayes.predict(X_test)

# Decision Tree model
decision_tree = DecisionTreeClassifier(criterion = 'entropy', min_samples_split = 2, max_depth= 11, random_state=0)
previsoes = decision_tree.predict(X_test)

# Random Forest model
random_forest = RandomForestClassifier(n_estimators = 100, min_samples_split = 7, max_depth= 11,  criterion = 'entropy', random_state = 0)
previsoes = random_forest.predict(X_test)

# Extra Tree model
extra_trees = ExtraTreesClassifier(n_estimators = 100, min_samples_split = 4, max_depth= 11, criterion = 'entropy', random_state = 0)
previsoes = extra_trees.predict(X_test)

# K Means model
kmeans_model = KMeans(n_clusters = 2, random_state= 0)
previsoes = kmeans_model.predict(X_test)

#  K Neighbors model
knn = KNeighborsClassifier(n_neighbors = 1, metric = 'minkowski', p = 2)
previsoes = knn.predict(X_test)

# Logistic Regression model
logistic = LogisticRegression(random_state = 1, max_iter=1000)
previsoes = logistic.predict(X_test)

#  Ada Boost model
ada_boost = AdaBoostClassifier(n_estimators = 500, learning_rate = 0.5, random_state = 0)
previsoes = ada_boost.predict(X_test)

# Gradient Boosting model
grad_boost = GradientBoostingClassifier(n_estimators = 300, learning_rate = 0.5, random_state = 0)
previsoes = grad_boost.predict(X_test)

# LGBM model
lgbm = LGBMClassifier(subsample = 0.5, reg_lambda = 0.3, reg_alpha = 0.1, num_leaves = 9, n_estimators = 500, min_child_weight = 7, min_child_samples = 9, max_depth = 4, learning_rate = 0.8, colsample_bytree = 0.9, random_state = 0)
previsoes = lgbm.predict(X_test)

# XGB model
xgb = XGBClassifier(subsample = 0.7, reg_lambda = 0.3, reg_alpha = 0.3, n_estimators = 500, min_child_weight = 3, max_depth = 6, learning_rate = 0.3, gamma = 0.9, colsample_bytree = 0.3, random_state = 0)
previsoes = xgb.predict(X_test)

