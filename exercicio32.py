# Exercício 32 – Validador de Cadastro com Typing

from typing import Dict, List, Any


def validar_cadastro(dados: Dict[str, Any]) -> Dict[str, List[str]]:
    """Valida os campos de um formulário de cadastro.

    Args:
        dados (Dict[str, Any]): Dicionário com os campos do cadastro.
            Esperado: nome (str), email (str), idade (int), cpf (str).

    Returns:
        Dict[str, List[str]]: Dicionário com duas listas:
            - "valido": campos que passaram na validação.
            - "erros": mensagens dos campos que falharam.

    Example:
        >>> validar_cadastro({"nome": "Ana", "email": "ana@email.com", "idade": 25, "cpf": "12345678901"})
        {'valido': ['nome', 'email', 'idade', 'cpf'], 'erros': []}
    """
    valido = []
    erros  = []

    # Valida nome
    nome = dados.get("nome", "")
    if len(nome) >= 3:
        valido.append("nome")
    else:
        erros.append("Nome deve ter ao menos 3 caracteres.")

    # Valida email
    email = dados.get("email", "")
    if "@" in email and "." in email:
        valido.append("email")
    else:
        erros.append("Email deve conter '@' e '.'.")

    # Valida idade
    idade = dados.get("idade", 0)
    if 18 <= idade <= 120:
        valido.append("idade")
    else:
        erros.append("Idade deve estar entre 18 e 120 anos.")

    # Valida CPF
    cpf = dados.get("cpf", "")
    if cpf.isdigit() and len(cpf) == 11:
        valido.append("cpf")
    else:
        erros.append("CPF deve conter exatamente 11 dígitos numéricos.")

    return {"valido": valido, "erros": erros}


# Testando com dados validos
print("=== Dados validos ===")
resultado = validar_cadastro({
    "nome": "Fernanda Costa",
    "email": "fernanda@empresa.com",
    "idade": 30,
    "cpf": "12345678901"
})
print(f"Campos ok : {resultado['valido']}")
print(f"Erros     : {resultado['erros']}")

# Testando com dados invalidos
print()
print("=== Dados invalidos ===")
resultado = validar_cadastro({
    "nome": "Fe",
    "email": "fernanda-sem-arroba",
    "idade": 15,
    "cpf": "123"
})
print(f"Campos ok : {resultado['valido']}")
print(f"Erros     : {resultado['erros']}")