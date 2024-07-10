import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("desafio_indicium_imdb.csv")
df.drop(columns=['Unnamed: 0'], inplace=True) # Removendo a coluna de índices

# print(df.describe())
# print(df.info())
# print(df.isnull().sum())

# Tratando coluna "Gross"
df['Gross'] = df['Gross'].str.replace(',', '').str.strip()
df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')

# Coluna "Gross" possui 169 linhas vazias

# Abordagem 1: Preencher com a média
#df['Gross'].fillna(df['Gross'].mean(), inplace=True)

# Abordagem 2: Dropar as linhas
# df.dropna(subset=['Gross'], inplace=True)

#Abordagem 3: Preencher com a mediana
df['Gross'].fillna(df['Gross'].median(), inplace=True)

# There are some empty cells in Gross, Meta Score and Certificate
# print(df.isnull().sum())
# df['Meta_score'].fillna(df['Meta_score'].mean(), inplace=True)
# df.dropna(inplace=True)

# Analyzing IMDB distribution
# plt.figure(figsize=(10, 6))
# sns.histplot(df['IMDB_Rating'], bins=20, kde=True)
# plt.title('IMDB Rating Distribution')
# plt.show()

# Analisando a nota IMDB de acordo com o diretor e os atores
director_ratings = df.groupby('Director')['IMDB_Rating'].mean().reset_index()
director_ratings = director_ratings.sort_values(by='IMDB_Rating', ascending=False)

# plt.figure(figsize=(12,6))
# plt.bar(director_ratings['Director'][:10], director_ratings['IMDB_Rating'][:10])
# plt.xlabel('Diretor')
# plt.ylabel('Média de IMDB_Rating')
# plt.title('Média de IMDB_Rating por Diretor (Top 10)')
# plt.xticks(rotation=45)
# plt.show()

director_count = df['Director'].value_counts()
directors_filter = director_count[director_count >= 7].index.tolist()
filtered_df = df[df['Director'].isin(directors_filter)]

print(df['IMDB_Rating'].mean())
print(filtered_df['IMDB_Rating'].mean())

# label_encoder = LabelEncoder()
#
# df['Director_Label'] = label_encoder.fit_transform(df['Director'])
#
# correlation = df['Director_Label'].corr(df['IMDB_Rating'])

# Correlation matrix
# correlation_matrix = df.corr()
#
# plt.figure(figsize=(10,6))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.show()


# print(correlation_matrix)

print('texto pro debug')