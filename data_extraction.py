import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("desafio_indicium_imdb.csv")

print(df.describe())
print(df.info())


df['Gross'].fillna(df['Gross'].mean(), inplace=True)

# There are some empty cells in Gross, Meta Score and Certificate
print(df.isnull().sum())
df['Meta_score'].fillna(df['Meta_score'].mean(), inplace=True)
df.dropna(inplace=True)

# Analyzing IMDB distribution
# plt.figure(figsize=(10, 6))
# sns.histplot(df['IMDB_Rating'], bins=20, kde=True)
# plt.title('IMDB Rating Distribution')
# plt.show()


# Correlation matrix
correlation_matrix = df.corr()

plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
# plt.show()


print(correlation_matrix)

print('texto pro debug')