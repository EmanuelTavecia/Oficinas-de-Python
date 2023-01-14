# EXERCÍCIO 6:

# Crie um programa que o usuário digite um número e mostre na tela sua tabuada.
# Requisito: utilizar o comando for.

# Resolução:

n = int(input('Digite um número: '))
for c in range(1, 11):
	print(f'{n} x {c} = {c*n}')
