# Exercício 27 – JSON com Múltiplos Registros

import json

# 1. Lista de funcionários
funcionarios = [
    {"nome": "Mariana Souza",  "cargo": "Analista de Dados",    "salario": 7850.00, "departamento": "TI"},
    {"nome": "Carlos Lima",    "cargo": "Dev Backend",           "salario": 9200.50, "departamento": "TI"},
    {"nome": "Fernanda Rocha", "cargo": "Product Manager",       "salario": 11400.00, "departamento": "Produto"},
]

# 2. Salvando em arquivo JSON
with open("funcionarios.json", "w", encoding="utf-8") as f:
    json.dump(funcionarios, f, indent=2, ensure_ascii=False)

print("Arquivo 'funcionarios.json' salvo!\n")

# 3. Lendo e exibindo em tabela
with open("funcionarios.json", "r", encoding="utf-8") as f:
    equipe = json.load(f)

def fmt(valor):
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")

print(f"{'Nome':<20} {'Cargo':<22} {'Depto':<12} {'Salário':>12}")
print("-" * 68)

for func in equipe:
    print(f"{func['nome']:<20} {func['cargo']:<22} {func['departamento']:<12} R$ {fmt(func['salario']):>11}")

# 4. Salário médio
media = sum(f["salario"] for f in equipe) / len(equipe)

print("-" * 68)
print(f"{'Salário médio da equipe':<55} R$ {fmt(media):>11}")