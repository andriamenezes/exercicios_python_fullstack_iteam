# Exercício 11 – Formatação Profissional com f-strings

nome    = "Geandria de Menezes"
cargo   = "Analista de Dados"
salario = 7850.50
anos    = 3

# Formata o salário no padrão brasileiro: R$ 7.850,50
salario_fmt = f"{salario:_.2f}".replace(".", ",").replace("_", ".")

print("=============================")
print("     FICHA DO FUNCIONÁRIO    ")
print("=============================")
print(f"Nome   : {nome}")
print(f"Cargo  : {cargo}")
print(f"Salário: R$ {salario_fmt}")
print(f"Tempo  : {anos} ano(s) de empresa")
print("=============================")