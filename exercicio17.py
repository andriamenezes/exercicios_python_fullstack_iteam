# Exercício 17 – Análise de Nota Fiscal

descricao  = input("Descrição do produto: ")
quantidade = int(input("Quantidade          : "))
preco_unit = float(input("Preço unitário  R$  : "))

subtotal = quantidade * preco_unit
imposto  = subtotal * 0.12
total    = subtotal + imposto

def fmt(valor):
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")

print()
print("===== NOTA FISCAL =====")
print(f"Produto   : {descricao}")
print(f"Quantidade: {quantidade} unidade(s)")
print(f"Preço Unit: R$ {fmt(preco_unit)}")
print(f"Subtotal  : R$ {fmt(subtotal)}")
print(f"Imposto   : R$ {fmt(imposto)}")
print(f"Total     : R$ {fmt(total)}")
print("=======================")