# Exercício 31 – Mesclando JSONs de Sistemas Diferentes

import json

cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
perfil   = {"id": 1042, "cargo": "Engenheira de Software", "nivel": "Senior",
            "salario": 12500.00, "habilidades": ["Python", "Django", "PostgreSQL"]}

# Mesclando os dois dicionários (o segundo sobrescreve chaves duplicadas)
funcionario_completo = {**cadastro, **perfil}

# Salvando em JSON
with open("funcionario_completo.json", "w", encoding="utf-8") as f:
    json.dump(funcionario_completo, f, indent=2, ensure_ascii=False)

print("Arquivo salvo com sucesso!\n")

# Lendo de volta
with open("funcionario_completo.json", "r", encoding="utf-8") as f:
    func = json.load(f)

def fmt(valor):
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")

print("=" * 35)
print("  FICHA DO FUNCIONARIO")
print("=" * 35)
print(f"  ID     : {func['id']}")
print(f"  Nome   : {func['nome']}")
print(f"  Email  : {func['email']}")
print(f"  Cargo  : {func['cargo']}")
print(f"  Nivel  : {func['nivel']}")
print(f"  Salario: R$ {fmt(func['salario'])}")
print("-" * 35)
print("  Habilidades:")
for i, habilidade in enumerate(func["habilidades"], start=1):
    print(f"    {i}. {habilidade}")
print("=" * 35)