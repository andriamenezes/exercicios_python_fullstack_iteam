# Exercício 09 – Boas-vindas Personalizada
 
nome  = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
 
ano_atual       = 2026
ano_nascimento  = ano_atual - idade
 
print(f"Olá, {nome}! Você tem {idade} anos e nasceu por volta de {ano_nascimento}.")