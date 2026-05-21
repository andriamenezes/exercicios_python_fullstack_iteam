# Exercício 19 – Manipulação de Strings no Mundo Real

email_bruto = " joao.silva@EMPRESA.com.br "

email_limpo = email_bruto.strip().lower()
usuario     = email_limpo.split("@")[0]
dominio     = email_limpo.split("@")[1]

print(f"E-mail bruto : '{email_bruto}'")
print(f"E-mail limpo : '{email_limpo}'")
print(f"Usuário      : '{usuario}'")
print(f"Domínio      : '{dominio}'")