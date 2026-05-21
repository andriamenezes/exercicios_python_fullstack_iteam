# Exercício 35 – Relatório de Vendas: JSON + Typing

import json
from typing import List


vendas_json = """
[
    {"mes": "Janeiro",  "produto": "Notebook", "quantidade": 45,  "valor_unit": 3200.00},
    {"mes": "Janeiro",  "produto": "Mouse",    "quantidade": 120, "valor_unit": 89.90},
    {"mes": "Fevereiro","produto": "Notebook", "quantidade": 38,  "valor_unit": 3200.00},
    {"mes": "Fevereiro","produto": "Teclado",  "quantidade": 75,  "valor_unit": 149.90},
    {"mes": "Marco",    "produto": "Monitor",  "quantidade": 30,  "valor_unit": 1200.00},
    {"mes": "Marco",    "produto": "Mouse",    "quantidade": 200, "valor_unit": 89.90}
]
"""


def calcular_total(venda: dict) -> float:
    """Retorna o total de uma venda (quantidade × valor unitário)."""
    return venda["quantidade"] * venda["valor_unit"]


def total_por_mes(vendas: List[dict]) -> dict:
    """Agrupa e soma os totais de vendas por mês."""
    resultado = {}
    for venda in vendas:
        mes   = venda["mes"]
        total = calcular_total(venda)
        resultado[mes] = resultado.get(mes, 0) + total
    return resultado


def produto_mais_vendido(vendas: List[dict]) -> str:
    """Retorna o produto com maior quantidade total vendida."""
    quantidades = {}
    for venda in vendas:
        produto = venda["produto"]
        quantidades[produto] = quantidades.get(produto, 0) + venda["quantidade"]
    return max(quantidades, key=lambda p: quantidades[p])


def fmt(valor: float) -> str:
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")


# Executando
vendas = json.loads(vendas_json)

print("=== TOTAL POR MES ===")
for mes, total in total_por_mes(vendas).items():
    print(f"  {mes:<12}: R$ {fmt(total)}")

print()
print(f"Produto mais vendido: {produto_mais_vendido(vendas)}")