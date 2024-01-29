import subprocess
from datetime import datetime

def mostrar_notificacao(titulo, mensagem):
    script = f'display notification "{mensagem}" with title "{titulo}"'
    subprocess.run(["osascript", "-e", script])

def alerta(nivel, base, etapa):
    # Definir o título com base no nível
    if nivel == 1:
        titulo = "Alerta Baixo"
    elif nivel == 2:
        titulo = "Alerta Médio"
    elif nivel == 3:
        titulo = "Alerta Alto"
    else:
        raise ValueError("O nível deve ser 1, 2 ou 3.")

    mensagem = f"Falha no carregamento da base {base} na etapa {etapa}."

    data_atual = datetime.now().strftime("%Y-%m-%d")
    mensagem += f"\nData da falha: {data_atual}"

    #notificacao
    mostrar_notificacao(titulo, mensagem)

alerta(2, "Cliente", "Extração")
