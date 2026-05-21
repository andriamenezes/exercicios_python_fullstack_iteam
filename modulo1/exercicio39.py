# Exercício 39 – Pipeline de Dados: JSON + Typing

import json


def carregar_dados(caminho: str) -> list[dict]:
    """Lê e retorna os dados brutos do arquivo JSON."""
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def normalizar_dados(dados: list[dict]) -> list[dict]:
    """Limpa espaços, corrige capitalização e formata o telefone."""
    def formatar_telefone(tel: str) -> str:
        t = tel.strip()
        if len(t) == 11:
            return f"({t[:2]}) {t[2:7]}-{t[7:]}"
        return f"({t[:2]}) {t[2:6]}-{t[6:]}"

    return [
        {
            **c,
            "nome":     c["nome"].strip().title(),
            "email":    c["email"].strip().lower(),
            "telefone": formatar_telefone(c["telefone"]),
            "cidade":   c["cidade"].strip().title(),
        }
        for c in dados
    ]


def enriquecer_dados(dados: list[dict]) -> list[dict]:
    """Adiciona o campo 'dominio' extraído do email."""
    return [
        {**c, "dominio": c["email"].split("@")[1]}
        for c in dados
    ]


def exportar_resultado(dados: list[dict], caminho: str) -> None:
    """Salva os dados processados em um novo arquivo JSON."""
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    print(f"Exportado para '{caminho}'.")


# Executando o pipeline
dados = carregar_dados("clientes_raw.json")
dados = normalizar_dados(dados)
dados = enriquecer_dados(dados)
exportar_resultado(dados, "clientes_processados.json")

# Exibindo resultado
print()
print(f"{'Nome':<18} {'Email':<25} {'Telefone':<16} {'Dominio'}")
print("-" * 72)
for c in dados:
    print(f"{c['nome']:<18} {c['email']:<25} {c['telefone']:<16} {c['dominio']}")