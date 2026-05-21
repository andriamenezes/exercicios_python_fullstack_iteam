# Exercício 33 – Sistema de Log em JSON

import json
from datetime import datetime


def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None:
    """Registra um evento no arquivo de log em formato JSON.

    Args:
        arquivo (str): Caminho do arquivo de log.
        nivel (str): Nível do evento. Ex: 'INFO', 'WARNING', 'ERROR'.
        mensagem (str): Descrição do evento ocorrido.

    Returns:
        None
    """
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    evento = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nivel": nivel.upper(),
        "mensagem": mensagem
    }

    logs.append(evento)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)


def ler_logs(arquivo: str) -> list:
    """Lê todos os eventos registrados no arquivo de log.

    Args:
        arquivo (str): Caminho do arquivo de log.

    Returns:
        list: Lista de dicionários com os eventos registrados.
    """
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def filtrar_por_nivel(logs: list, nivel: str) -> list:
    """Filtra os eventos de log por nível.

    Args:
        logs (list): Lista de eventos retornada por ler_logs().
        nivel (str): Nível desejado. Ex: 'INFO', 'WARNING', 'ERROR'.

    Returns:
        list: Lista apenas com os eventos do nível informado.
    """
    return [log for log in logs if log["nivel"] == nivel.upper()]


# Registrando 5 eventos
ARQUIVO = "sistema.log.json"

registrar_evento(ARQUIVO, "INFO",    "Sistema iniciado com sucesso.")
registrar_evento(ARQUIVO, "INFO",    "Conexao com banco de dados estabelecida.")
registrar_evento(ARQUIVO, "WARNING", "Uso de memoria acima de 75%.")
registrar_evento(ARQUIVO, "ERROR",   "Falha ao conectar na API de pagamento.")
registrar_evento(ARQUIVO, "WARNING", "Tentativa de login invalida para usuario 'admin'.")

# Lendo todos os logs
todos = ler_logs(ARQUIVO)

print(f"Total de eventos registrados: {len(todos)}\n")
print(f"{'Timestamp':<22} {'Nivel':<10} Mensagem")
print("-" * 70)
for log in todos:
    print(f"{log['timestamp']:<22} {log['nivel']:<10} {log['mensagem']}")

# Filtrando por nível
print()
for nivel in ["INFO", "WARNING", "ERROR"]:
    filtrados = filtrar_por_nivel(todos, nivel)
    print(f"[{nivel}] {len(filtrados)} evento(s):")
    for log in filtrados:
        print(f"  {log['timestamp']} — {log['mensagem']}")