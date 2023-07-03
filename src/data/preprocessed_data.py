import pandas as pd
import numpy as np

df = pd.read_csv('../data/raw/Customer-Churn-Records.csv', sep = ',')
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis = 1)

# OneHot Label Encoding
hot = pd.get_dummies(df[['Geography', 'Gender', 'Card Type']])

df = pd.concat([df, hot], axis = 1)
df = df.drop(['Geography', 'Gender', 'Card Type'], axis = 1)