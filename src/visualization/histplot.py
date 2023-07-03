import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../data/raw/Customer-Churn-Records.csv', sep = ',')

plt.figure(figsize = (15, 12))

plt.subplot(3, 2, 1)
sns.histplot(x = df['CreditScore'], kde = True)

plt.subplot(3, 2, 2)
sns.histplot(x = df['Age'], kde = True)

plt.subplot(3, 2, 3)
sns.histplot(x = df['Balance'], kde = True)

plt.subplot(3, 2, 4)
sns.histplot(x = df['EstimatedSalary'], kde = True)

plt.subplot(3, 2, 5)
sns.histplot(x = df['Point Earned'], kde = True)
