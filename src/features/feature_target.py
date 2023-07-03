import pandas as pd

df = pd.read_csv('../data/raw/Customer-Churn-Records.csv', sep = ',')
X = df.drop('Exited', axis = 1)
X = X.values
y = df['Exited']