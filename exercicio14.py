# Exercício 14 – Troca de Variáveis

# Código com bug
a = 10
b = 20
a = b       # a vira 20... mas o 10 se perdeu!
b = a       # b recebe 20 de novo — troca não acontece
print("Bug:          ", a, b)   # 20 20

print()

# Forma 1 – Variável auxiliar
a = 10
b = 20
aux = a     # guarda o 10 antes de sobrescrever
a = b       # a vira 20
b = aux     # b recebe o 10 guardado
print("Com auxiliar: ", a, b)   # 20 10

print()

# Forma 2 – Idiomático Python
a = 10
b = 20
a, b = b, a     # Python avalia o lado direito antes de atribuir
print("Pythônico:    ", a, b)   # 20 10