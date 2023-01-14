# EXERCÍCIO 2:

# Crie um programa que pense em dois números inteiros
# entre 0 e 50 aleatórios e em seguida faça a soma entre eles.
# Exiba na tela a operação, de forma organizada.

# Resolução:

import random

n1 = random.randint(0, 50)
n2 = random.randint(0, 50)
s = n1 + n2
print(f'{n1} + {n2} = {s}')