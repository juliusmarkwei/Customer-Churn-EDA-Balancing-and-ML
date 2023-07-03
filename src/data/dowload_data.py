
import pandas as pd

df = pd.read_csv('../data/raw/Customer-Churn-Records.csv', sep = ',')
df.head(5)
df.info()
