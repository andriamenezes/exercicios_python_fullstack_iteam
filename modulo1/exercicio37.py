# Exercício 37 – Serialização Customizada de Objetos para JSON

import json
from datetime import datetime


class Produto:
    def __init__(self, nome: str, preco: float, criado_em: datetime):
        self.nome      = nome
        self.preco     = preco
        self.criado_em = criado_em

    def __repr__(self):
        return f"Produto(nome={self.nome!r}, preco={self.preco}, criado_em={self.criado_em})"


def produto_para_dict(produto: Produto) -> dict:
    """Converte um Produto para dicionário serializável em JSON."""
    return {
        "nome":      produto.nome,
        "preco":     produto.preco,
        "criado_em": produto.criado_em.isoformat()   # datetime → string ISO
    }


def dict_para_produto(dados: dict) -> Produto:
    """Converte um dicionário de volta para um objeto Produto."""
    return Produto(
        nome      = dados["nome"],
        preco     = dados["preco"],
        criado_em = datetime.fromisoformat(dados["criado_em"])  # string ISO → datetime
    )


# Lista de produtos
produtos = [
    Produto("Notebook",  3200.00, datetime(2025, 1, 10, 9, 0)),
    Produto("Mouse",       89.90, datetime(2025, 2, 5, 14, 30)),
    Produto("Teclado",    149.90, datetime(2025, 3, 20, 11, 15)),
]

# Serializar para JSON
lista_dict = [produto_para_dict(p) for p in produtos]
json_str   = json.dumps(lista_dict, indent=2, ensure_ascii=False)

print("=== JSON gerado ===")
print(json_str)

# Desserializar de volta para objetos
produtos_restaurados = [dict_para_produto(d) for d in json.loads(json_str)]

print("=== Objetos restaurados ===")
for p in produtos_restaurados:
    print(f"  {p.nome:<12} R$ {p.preco:>8.2f}  criado em {p.criado_em.strftime('%d/%m/%Y')}")