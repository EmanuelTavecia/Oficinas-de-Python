# EXERCÍCIO 9:

# Crie um programa que o usuário digite números.
# O programa encerra quando for digitado 0.
# Ao final, mostre a soma de todos os números digitados.
# Resposta final esperada: A soma de todos os números é n.

# Resolução 1:

n = float(input('Digite um número: '))
s = 0
while n != 0:
    s += n
    n = float(input('Digite um número: '))
print(f'A soma de todos os números é {s}')

# Resolução 2:

s = 0
while True:
    n = float(input('Digite um número: '))
    s += n
    if n == 0:
        break
print(f'A soma de todos os números é {s}')
