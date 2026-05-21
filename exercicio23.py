# Exercício 23 – Lendo um JSON Simples

import json

aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}

# Dicionário → JSON (texto)
aluno_json = json.dumps(aluno, indent=2)

print("=== JSON gerado ===")
print(aluno_json)

# JSON (texto) → Dicionário
aluno_dict = json.loads(aluno_json)

media = sum(aluno_dict["notas"]) / len(aluno_dict["notas"])

print()
print("=== Dados extraídos ===")
print(f"Nome : {aluno_dict['nome']}")
print(f"Média: {media:.2f}")