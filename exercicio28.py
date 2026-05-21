# Exercício 28 – Docstring Google Style + Juros Compostos

def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    """Calcula o montante final com juros compostos.

    Args:
        capital (float): Valor inicial investido em reais. Deve ser positivo.
        taxa (float): Taxa de juros ao período em percentual (ex: 2.5 para 2.5%).
                      Deve ser positiva.
        periodo (int): Número de períodos (meses, anos, etc.).

    Returns:
        float: Montante final após a aplicação dos juros compostos.

    Raises:
        ValueError: Se capital for negativo ou zero.
        ValueError: Se taxa for negativa.

    Example:
        >>> calcular_juros_compostos(1000.0, 2.5, 12)
        1344.89
    """
    if capital <= 0:
        raise ValueError(f"Capital deve ser positivo. Recebido: {capital}")
    if taxa < 0:
        raise ValueError(f"Taxa não pode ser negativa. Recebida: {taxa}")

    return capital * (1 + taxa / 100) ** periodo


# Testando a função
montante = calcular_juros_compostos(1000.0, 2.5, 12)
juros    = montante - 1000.0

print(f"Capital inicial : R$ 1.000,00")
print(f"Taxa            : 2.5% ao período")
print(f"Períodos        : 12")
print(f"Juros obtidos   : R$ {juros:.2f}")
print(f"Montante final  : R$ {montante:.2f}")

# Testando o Raises
print()
try:
    calcular_juros_compostos(-500, 2.5, 12)
except ValueError as e:
    print(f"Erro capturado: {e}")