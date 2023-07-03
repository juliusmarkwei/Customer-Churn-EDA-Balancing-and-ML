import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('../data/raw/Customer-Churn-Records.csv', sep = ',')
X = df.drop('Exited', axis = 1)
X = X.values

scaler = StandardScaler()
X_standard = scaler.fit_transform(X)
