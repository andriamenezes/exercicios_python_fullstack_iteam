# Exercício 21 – Sua Primeira Função com Docstring

def saudacao(nome):
    """
    Retorna uma mensagem de boas-vindas personalizada.

    Args:
        nome (str): Nome da pessoa a ser saudada.

    Returns:
        str: String com a mensagem de boas-vindas.

    Example:
        >>> saudacao("Ana")
        'Olá, Ana! Seja bem-vinda ao curso.'
    """
    return f"Olá, {nome}! Seja bem-vinda ao curso."


print(saudacao("Ana"))
print(saudacao("Carlos"))
print(saudacao("Mariana"))

# Bônus: exibindo a docstring da função
print()
print("--- Documentação da função ---")
print(saudacao.__doc__)