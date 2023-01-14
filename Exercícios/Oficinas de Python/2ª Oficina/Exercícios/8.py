# EXERCÍCIO 8:

# Crie um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior peso e o menor peso lidos.

# Resolução:

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso foi {maior} e o menor peso foi {menor}.')