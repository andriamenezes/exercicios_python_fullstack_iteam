# Exercício 15 – Calculadora de Desconto

valor_compra = float(input("Digite o valor da compra: R$ "))

desconto    = valor_compra * 0.10
valor_final = valor_compra - desconto

# Formata no padrão brasileiro
def fmt(valor):
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")

print()
print(f"Valor original : R$ {fmt(valor_compra)}")
print(f"Desconto (10%) : R$ {fmt(desconto)}")
print(f"Valor final    : R$ {fmt(valor_final)}")