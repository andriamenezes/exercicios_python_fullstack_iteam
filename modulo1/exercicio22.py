# Exercício 22 – Type Hints Básico

def calcular_area(largura: float, altura: float) -> float:
    return largura * altura

def formatar_nome(nome: str, sobrenome: str) -> str:
    return f"{nome} {sobrenome}".title()

def eh_maior_de_idade(idade: int) -> bool:
    return idade >= 18


# Testando as funções
print(calcular_area(5.0, 3.0))
print(formatar_nome("joao", "SILVA"))
print(eh_maior_de_idade(20))
print(eh_maior_de_idade(15))