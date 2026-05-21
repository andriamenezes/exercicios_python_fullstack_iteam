# Exercício 36 – Agenda de Contatos: CRUD em JSON

import json

ARQUIVO = "contatos.json"


def _ler() -> list:
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _salvar(contatos: list) -> None:
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=2, ensure_ascii=False)


def adicionar_contato(nome: str, telefone: str, email: str) -> None:
    """Adiciona um novo contato à agenda."""
    contatos = _ler()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    _salvar(contatos)
    print(f"Contato '{nome}' adicionado.")


def listar_contatos() -> list:
    """Retorna todos os contatos da agenda."""
    return _ler()


def buscar_contato(nome: str) -> dict | None:
    """Busca um contato pelo nome. Retorna None se não encontrar."""
    for contato in _ler():
        if contato["nome"].lower() == nome.lower():
            return contato
    return None


def remover_contato(nome: str) -> bool:
    """Remove um contato pelo nome. Retorna True se removeu, False se não encontrou."""
    contatos  = _ler()
    restantes = [c for c in contatos if c["nome"].lower() != nome.lower()]
    if len(restantes) == len(contatos):
        return False
    _salvar(restantes)
    return True


# Demonstração

# Adicionar
print("=== ADICIONAR ===")
adicionar_contato("Ana Lima",    "(11) 91234-5678", "ana@email.com")
adicionar_contato("Carlos Melo", "(21) 98765-4321", "carlos@email.com")
adicionar_contato("Bia Souza",   "(31) 99999-0000", "bia@email.com")

# Listar
print()
print("=== LISTAR ===")
for c in listar_contatos():
    print(f"  {c['nome']:<15} {c['telefone']}  {c['email']}")

# Buscar
print()
print("=== BUSCAR ===")
resultado = buscar_contato("Carlos Melo")
if resultado:
    print(f"  Encontrado: {resultado}")
else:
    print("  Nao encontrado.")

# Remover
print()
print("=== REMOVER ===")
removido = remover_contato("Bia Souza")
print(f"  'Bia Souza' removida: {removido}")

print()
print("=== LISTA FINAL ===")
for c in listar_contatos():
    print(f"  {c['nome']:<15} {c['telefone']}  {c['email']}")