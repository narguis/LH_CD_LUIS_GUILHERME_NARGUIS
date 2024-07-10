import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("desafio_indicium_imdb.csv")

# There are some empty cells in Gross, Meta Score and Certificate
# print(df.isnull().sum())
# df['Meta_score'].fillna(df['Meta_score'].mean(), inplace=True)
# df.dropna(inplace=True)

# Analyzing IMDB distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['IMDB_Rating'], bins=20, kde=True)
plt.title('IMDB Rating Distribution')
plt.show()


print('texto pro debug')