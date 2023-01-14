# EXERCÍCIO 1:

# Crie um programa que leia 3 números,
# calcule a raiz quadrada de todos os números
# e exiba na tela os números e suas respectivas raízes, de forma organizada.

# Resolução:

import math

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
r1 = math.sqrt(n1)
r2 = math.sqrt(n2)
r3 = math.sqrt(n3)
print(f'A raiz de {n1} é {r1}')
print(f'A raiz de {n2} é {r2}')
print(f'A raiz de {n3} é {r3}')