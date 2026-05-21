# Exercício 26 – Typing com Optional e Union

from typing import Optional, Union

def buscar_usuario(id: int, nome: Optional[str] = None) -> Optional[dict]:
    """
    Busca um usuário pelo id e nome opcional.

    Args:
        id (int): Identificador do usuário. Deve ser positivo.
        nome (Optional[str]): Nome do usuário. Pode ser None.

    Returns:
        Optional[dict]: Dicionário com os dados do usuário,
                        ou None se o id for negativo.

    Example:
        >>> buscar_usuario(1, "Ana")
        {'id': 1, 'nome': 'Ana', 'status': 'ativo'}

        >>> buscar_usuario(-1)
        None
    """
    if id < 0:
        return None

    return {
        "id": id,
        "nome": nome if nome is not None else "Não informado",
        "status": "ativo"
    }


# Testando os cenários
print(buscar_usuario(1, "Ana"))
print(buscar_usuario(2, None))
print(buscar_usuario(3))
print(buscar_usuario(-1, "Carlos"))