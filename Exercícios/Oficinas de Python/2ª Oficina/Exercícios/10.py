# EXERCÍCIO 10:

# Crie um programa que leia números inteiros
# até que o usuário insira um valor par.
# No final, deve-se mostrar a quantidade
# e a soma de todos os números ímpares digitados.

# Resolução:

s = 0
c = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n % 2 != 0:
        s += n
        c += 1
    else:
        break
print(f'A soma dos {c} números é {s}.')
