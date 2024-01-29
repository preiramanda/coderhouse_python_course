# Projeto final Coderhouse

## Objetivo
Esse projeto tem como objetivo ler dados de uma API aberta (https://restcountries.com/v3.1) que contém dados de diferentes países.
Vamos escolher os 3 primeiros países da API, limpar e tratar os dados disponiveis e criar 3 tabelas (uma para cada país) em um banco SQLite.

## 🚀 Contexto

O projeto conta com arquivo “api.py” que realiza a conexão na API aberta e com a biblioteca “subprocess” gera um alerta informando o status da conexão (tanto para computadores windows/mac). O projeto também conta com o arquivo “banco_de_dados.py” onde ao executar o script realiza a criação do banco de dados com as tabelas definidas gerando o arquivo “dados_api.db”. Por fim o arquivo “tratamento_das_bases.py” realiza a padronização e tratamento dos dados recebidos da API aberta como ajustes das colunas, tratamento de variáveis, ajuste de valores “missing” (valores nulos que serão convertidos em 0) e remoção dos espaçamentos em branco. Em seguida, o script realiza a inserção das tabelas tratadas no banco de dados SQLite. 

No projeto há o arquivo “requirements.txt” onde contém todas as bibliotecas utilizadas neste projeto.

## 🔧 Instalação

Realizar a instalação das bibliotecas contidas no arquivo requirements.txt e a ativação da “env”;

### Ordem de execução:
1. Executar o arquivo banco_de_dados.py que vai criar o schema e tabelas no SQLite. O arquivo dados_api.db será gerado, confirmando a criação do banco de dados;
2. Executar o arquivo api.py para conectar a API;
3. Executar o arquivo tratamento_das_bases para limpar os dados da API e popular o banco de dados.
