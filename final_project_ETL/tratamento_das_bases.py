import pandas as pd
import sqlite3
from api import tabela1, tabela2, tabela3  # Importar tabelas do arquivo api.py

# Definir função para ajustar os dados
def ajustar_dados(tabela, tabela_nome):
    # Ajustar nomes de colunas
    tabela.rename(columns={'Nome do País': 'Nome', 'Capital': 'Capital', 'População': 'Populacao'}, inplace=True)

    # Tratar tipos de variáveis
    tabela['Populacao'] = pd.to_numeric(tabela['Populacao'], errors='coerce')

    # Ajustar missing
    tabela.fillna(0, inplace=True)  # Substituir missing por zero

    # Tratar colunas de string (remover espaços em branco)
    tabela['Nome'] = tabela['Nome'].str.strip()
    tabela['Capital'] = tabela['Capital'].str.strip()

    # Salvar no SQLite
    conn = sqlite3.connect('dados_api.db')  # Conectar ao banco de dados existente
    cursor = conn.cursor()

    # Inserir dados na tabela existente
    tabela.to_sql(tabela_nome, conn, index=False, if_exists='replace') 
    conn.commit()
    conn.close()

# Ajustar tabelas e salvar no SQLite
ajustar_dados(tabela1, 'country1')
ajustar_dados(tabela2, 'country2')
ajustar_dados(tabela3, 'country3')
