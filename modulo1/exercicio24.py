# Exercício 24 – Conversor de Moeda com Typing e Docstring

def converter_moeda(valor_brl: float) -> tuple[float, float]:
    """
    Converte um valor em reais para dólar e euro.

    Args:
        valor_brl (float): Valor em reais (BRL) a ser convertido.

    Returns:
        tuple[float, float]: Tupla com (valor_usd, valor_eur).

    Example:
        >>> converter_moeda(515.0)
        (100.0, 92.29)
    """
    USD = 5.15
    EUR = 5.58

    valor_usd = valor_brl / USD
    valor_eur = valor_brl / EUR

    return valor_usd, valor_eur


# Testando a função
valor = 1000.0
usd, eur = converter_moeda(valor)

print(f"Valor original : R$ {valor:.2f}")
print(f"Em dólar       : $ {usd:.2f}")
print(f"Em euro        : € {eur:.2f}")