# Exercício 30 – Typing Avançado: TypedDict

import json
from typing import TypedDict, List


class ItemPedido(TypedDict):
    produto: str
    quantidade: int
    preco_unitario: float


class Pedido(TypedDict):
    id_pedido: int
    cliente: str
    itens: List[ItemPedido]
    status: str


# Criando um pedido de exemplo
pedido: Pedido = {
    "id_pedido": 1042,
    "cliente": "Ana Paula Ferreira",
    "itens": [
        {"produto": "Teclado Mecânico",  "quantidade": 1, "preco_unitario": 349.90},
        {"produto": "Mouse Gamer",        "quantidade": 1, "preco_unitario": 189.50},
        {"produto": "Cabo USB-C",         "quantidade": 2, "preco_unitario":  39.90},
    ],
    "status": "aprovado"
}

# Serializando para JSON
pedido_json = json.dumps(pedido, indent=2, ensure_ascii=False)

# Calculando o total
total = sum(item["quantidade"] * item["preco_unitario"] for item in pedido["itens"])

def fmt(valor: float) -> str:
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")

# Exibindo o boletim
print("=" * 42)
print("  RESUMO DO PEDIDO")
print("=" * 42)
print(f"  Pedido   : #{pedido['id_pedido']}")
print(f"  Cliente  : {pedido['cliente']}")
print(f"  Status   : {pedido['status'].upper()}")
print("-" * 42)
print(f"  {'Produto':<20} {'Qtd':>4}  {'Subtotal':>10}")
print("-" * 42)

for item in pedido["itens"]:
    subtotal = item["quantidade"] * item["preco_unitario"]
    print(f"  {item['produto']:<20} {item['quantidade']:>4}  R$ {fmt(subtotal):>9}")

print("-" * 42)
print(f"  {'TOTAL':<26} R$ {fmt(total):>9}")
print("=" * 42)

print()
print("JSON gerado:")
print(pedido_json)