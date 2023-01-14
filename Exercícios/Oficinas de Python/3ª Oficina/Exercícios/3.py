# EXERCÍCIO 3:

# Crie um programa que faça uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 a 0,
# com uma pausa de 1 segundo entre eles.

# Resolução:

import time

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('BOOM')
