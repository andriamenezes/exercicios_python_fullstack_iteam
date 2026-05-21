# Exercício 38 – Typing com Callable e Generics

from typing import TypeVar, List, Callable

T = TypeVar("T")
R = TypeVar("R")


def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
    """Aplica uma função a cada item da lista e retorna a lista transformada.

    Args:
        dados (List[T]): Lista de entrada com qualquer tipo.
        funcao (Callable[[T], R]): Função a ser aplicada em cada item.

    Returns:
        List[R]: Nova lista com os resultados.
    """
    return [funcao(item) for item in dados]


# 1. Strings → maiúsculas
nomes = ["ana", "carlos", "fernanda"]
resultado = aplicar_transformacao(nomes, str.upper)
print("Maiúsculas :", resultado)

# 2. Floats → arredondados com 2 casas
precos = [3.14159, 89.9999, 149.005]
resultado = aplicar_transformacao(precos, lambda x: round(x, 2))
print("Arredondado:", resultado)

# 3. Dicionários → extraindo o campo "nome"
produtos = [
    {"nome": "Notebook", "preco": 3200},
    {"nome": "Mouse",    "preco": 89},
    {"nome": "Teclado",  "preco": 149},
]
resultado = aplicar_transformacao(produtos, lambda d: d["nome"])
print("Nomes      :", resultado)