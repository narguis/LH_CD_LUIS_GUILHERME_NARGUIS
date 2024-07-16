Projeto de Análise Exploratória e Modelo de Previsão de Ratings de Filmes
Este projeto consiste em uma análise exploratória dos dados de filmes e um modelo de previsão de ratings de filmes utilizando regressão linear. O projeto está dividido em dois componentes principais:

analise_exploratoria.ipynb: Um notebook Jupyter que realiza a análise exploratória dos dados.
Modelo_Luis_Narguis.pkl: Um modelo treinado de regressão linear salvo em um arquivo .pkl.
Estrutura do Projeto
Copy code
.
├── analise_exploratoria.ipynb
├── Modelo_Luis_Narguis.pkl
├── desafio_indicium_imdb.csv
├── requirements.txt
└── README.md
Requisitos
Para executar o projeto, você precisará ter instalado:

Python 3.6 ou superior
Jupyter Notebook
As bibliotecas listadas no arquivo requirements.txt
Configuração do Ambiente
Passo 1: Clonar o Repositório
Clone este repositório em sua máquina local usando:

bash
Copy code
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Passo 2: Criar um Ambiente Virtual (opcional, mas recomendado)
Crie e ative um ambiente virtual para manter suas dependências organizadas.

bash
Copy code
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
Passo 3: Instalar as Dependências
Instale as dependências listadas no arquivo requirements.txt:

bash
Copy code
pip install -r requirements.txt
Executar a Análise Exploratória
Abra o Jupyter Notebook para executar a análise exploratória:

bash
Copy code
jupyter notebook analise_exploratoria.ipynb
Navegue até o notebook analise_exploratoria.ipynb e execute as células para realizar a análise exploratória dos dados.

Usar o Modelo Treinado
O modelo treinado de regressão linear está salvo no arquivo Modelo_Luis_Narguis.pkl. Você pode carregar e usar este modelo para fazer previsões.

Exemplo de Uso do Modelo
Aqui está um exemplo de como carregar o modelo e fazer uma previsão:

python
Copy code
import pandas as pd
import numpy as np
import joblib

# Carregar o modelo
modelo = joblib.load('Modelo_Luis_Narguis.pkl')

# Exemplo de dados de entrada
shawshank = {
 'Runtime': 142,
 'Meta_score': 80.0,
 'No_of_Votes': 2343110,
}

shawshank_df = pd.DataFrame([shawshank])

# Aplicar a transformação logarítmica
for feature in ['Runtime', 'Meta_score', 'No_of_Votes']:
    shawshank_df[feature] = np.log(shawshank_df[feature] + 1)

# Fazer a previsão
predicted_rating = modelo.predict(shawshank_df)
print(f"Predicted IMDB Rating for 'The Shawshank Redemption': {predicted_rating[0]}")
