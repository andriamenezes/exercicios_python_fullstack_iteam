# Exercício 34 – Configuração de Aplicação via JSON

import json


def carregar_config(caminho: str) -> dict:
    """Lê e retorna o arquivo de configuração JSON."""
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def obter_valor(config: dict, chave: str, padrao=None):
    """Navega por chaves aninhadas usando notação de ponto.

    Exemplo: 'app.versao' retorna config['app']['versao'].
    Retorna `padrao` se a chave não existir.
    """
    partes = chave.split(".")
    valor  = config

    for parte in partes:
        if isinstance(valor, dict) and parte in valor:
            valor = valor[parte]
        else:
            return padrao

    return valor


# Demonstração
config = carregar_config("config.json")

print(obter_valor(config, "app.nome"))
print(obter_valor(config, "app.versao"))
print(obter_valor(config, "banco.porta"))
print(obter_valor(config, "email.servidor"))
print(obter_valor(config, "app.timeout", padrao=30))   # chave inexistente → usa padrão