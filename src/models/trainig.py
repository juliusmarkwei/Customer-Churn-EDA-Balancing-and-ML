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

# naaaive bayes model
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)

# Decison tree model
decision_tree = DecisionTreeClassifier(criterion = 'entropy', min_samples_split = 2, max_depth= 11, random_state=0)
decision_tree.fit(X_train, y_train)

# Random Forest model
random_forest = RandomForestClassifier(n_estimators = 100, min_samples_split = 7, max_depth= 11,  criterion = 'entropy', random_state = 0)
random_forest.fit(X_train, y_train)

# Extra Trees model
extra_trees = ExtraTreesClassifier(n_estimators = 100, min_samples_split = 4, max_depth= 11, criterion = 'entropy', random_state = 0)
extra_trees.fit(X_train, y_train)

# K Means Clusssstering 
kmeans_model = KMeans(n_clusters = 2, random_state= 0)
kmeans_model.fit(X_train)

# K Neighnors model
knn = KNeighborsClassifier(n_neighbors = 1, metric = 'minkowski', p = 2)
knn.fit(X_train, y_train)

# Logistic Regression model
logistic = LogisticRegression(random_state = 1, max_iter=1000)
logistic.fit(X_train, y_train)

#  Ada Boost model
ada_boost = AdaBoostClassifier(n_estimators = 500, learning_rate = 0.5, random_state = 0)
ada_boost.fit(X_train, y_train)

# Gradient Boosting Model
grad_boost = GradientBoostingClassifier(n_estimators = 300, learning_rate = 0.5, random_state = 0)
grad_boost.fit(X_train, y_train)

# LBBM Model
lgbm = LGBMClassifier(subsample = 0.5, reg_lambda = 0.3, reg_alpha = 0.1, num_leaves = 9, n_estimators = 500, min_child_weight = 7, min_child_samples = 9, max_depth = 4, learning_rate = 0.8, colsample_bytree = 0.9, random_state = 0)
lgbm.fit(X_train, y_train)

# XGBoost model
xgb = XGBClassifier(subsample = 0.7, reg_lambda = 0.3, reg_alpha = 0.3, n_estimators = 500, min_child_weight = 3, max_depth = 6, learning_rate = 0.3, gamma = 0.9, colsample_bytree = 0.3, random_state = 0)
xgb.fit(X_train, y_train)
