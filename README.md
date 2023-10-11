# Explorando Pipeline de etl com Py
### Sobre:
Estou atualmente aprendendo ETL e Python e estou explorando ativamente os recursos e práticas no contexto da Santander Dev Week 2023 Ministrado DIO.ME

### Proposta: 

Este projeto visa  demostra os encinamentos adiquiridos no curso Explorando IA Generativa em um Pipeline de ETL com Python


### Linguagem Utilizada:
###
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white&color=black)

### Bibliotecas Utilizadas:
###
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white&color=black) 

### Metodologia:
- **Coleta e Aquisição dos Dados:**
  Utilizando um arquivo chamado "dados.csv" que contém informações como ID, nomes e idades dos usuários.
  ```python
  data = pd.read_csv('dados.csv')

- **Transformação dos Dados:**
  Aplicamos a transformação para converter os nomes em letras maiúsculas. Isso é feito com o seguinte código:
  ```python
  data['nome'] = data['nome'].str.upper()

- **Exibição dos Dados Transformados:**
   ```python
   print(data)
- **Conclusão:**
- Este projeto oferece uma visão prática da aplicação de conceitos de ETL utilizado Python,este    projeto é apenas um ponto de partida para o meu aprendizado
