# Importando libs necessárias
import requests
import pandas as pd
import subprocess
from datetime import datetime

# Função para que eu consiga notificar se houve conexão com a API
def mostrar_notificacao(titulo, mensagem):
    script = f'display notification "{mensagem}" with title "{titulo}"'
    subprocess.run(["osascript", "-e", script])

# Funçaõ para conectar a API
def obter_dados_pais(nome_pais):
    url = f'https://restcountries.com/v3.1/name/{nome_pais}'
    resposta = requests.get(url)
    dados_pais = resposta.json()
    return dados_pais

# Verificando a conexão com a API
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

# If para checar conexão
if response.status_code == 200:
    data_json = response.json()
    api_acessada = True
    mostrar_notificacao("Alerta de Conexão", "API acessada.")

else:
    print("Não foi possível acessar a API")
    api_acessada = False
    mostrar_notificacao("Alerta de Conexão", "Não foi possível acessar a API.")

# Se a API foi acessada com sucesso
if api_acessada:
    # Extraindo informações de três países diferentes
    pais1 = obter_dados_pais(data_json[0]['name']['common'])
    pais2 = obter_dados_pais(data_json[1]['name']['common'])
    pais3 = obter_dados_pais(data_json[2]['name']['common'])

    # Criar tabelas usando pandas
    tabela1 = pd.DataFrame({
        'Nome do País': [pais1[0]['name']['common']],
        'Capital': [pais1[0]['capital'][0]],
        'População': [pais1[0]['population']],
    })

    tabela2 = pd.DataFrame({
        'Nome do País': [pais2[0]['name']['common']],
        'Capital': [pais2[0]['capital'][0]],
        'População': [pais2[0]['population']],
    })

    tabela3 = pd.DataFrame({
        'Nome do País': [pais3[0]['name']['common']],
        'Capital': [pais3[0]['capital'][0]],
        'População': [pais3[0]['population']],
    })

    # Exibir as tabelas
    print('Tabela 1:')
    print(tabela1)

    print('Tabela 2:')
    print(tabela2)

    print('Tabela 3:')
    print(tabela3)
