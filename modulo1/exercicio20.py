# Exercício 20 – Calculadora de Investimento Simples

capital = float(input("Capital inicial (R$)      : "))
taxa    = float(input("Taxa de juros ao mês (%)  : "))
meses   = int(input("Período (meses)           : "))

i = taxa / 100
montante = capital * (1 + i * meses)
juros    = montante - capital

def fmt(valor):
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")

print()
print("===== INVESTIMENTO SIMPLES =====")
print(f"Capital inicial : R$ {fmt(capital)}")
print(f"Taxa de juros   : {taxa:.2f}% ao mês")
print(f"Período         : {meses} mês(es)")
print("--------------------------------")
print(f"Juros totais    : R$ {fmt(juros)}")
print(f"Montante final  : R$ {fmt(montante)}")
print("================================")