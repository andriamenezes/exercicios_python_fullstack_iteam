# Exercício 25 – Salvando Dados em JSON

import json

# 1. Criando o dicionário do produto
produto = {
    "id": 101,
    "nome": "Teclado Mecânico RGB",
    "preco": 349.90,
    "estoque": 42,
    "disponivel": True,
    "categorias": ["Periféricos", "Informática", "Gaming"]
}

# 2. Salvando em arquivo JSON
with open("produto.json", "w", encoding="utf-8") as f:
    json.dump(produto, f, indent=2, ensure_ascii=False)

print("Arquivo 'produto.json' salvo com sucesso!")
print()

# 3. Lendo o arquivo de volta
with open("produto.json", "r", encoding="utf-8") as f:
    produto_lido = json.load(f)

print("=== Dados do Produto ===")
print(f"ID          : {produto_lido['id']}")
print(f"Nome        : {produto_lido['nome']}")
print(f"Preço       : R$ {produto_lido['preco']:.2f}")
print(f"Estoque     : {produto_lido['estoque']} unidades")
print(f"Disponível  : {produto_lido['disponivel']}")
print(f"Categorias  : {', '.join(produto_lido['categorias'])}")