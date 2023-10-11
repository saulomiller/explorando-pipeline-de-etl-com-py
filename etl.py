import pandas as pd

# Extração do  dados.csv
data = pd.read_csv('dados.csv')

# transformação dos dados
data['nome'] = data['nome'].str.upper()

# Exibição dos dados transformados
print(data)
 