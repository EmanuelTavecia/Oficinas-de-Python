# EXERCÍCIO 5:

# Faça um programa em que o usuário digite 2 números inteiros
# e logo em seguida escolha qual operação deve ser realizada:
# 1 - Adição, 2 - Subtração, 3 - Multiplicação ou 4 - Divisão.
# O programa deverá realizar a operação e exibir o resultado da seguinte forma: x + y = z.

# Resolução:

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = int(input('''Digite a operação:
1 - Adição;
2 - Subtração;
3 - Multiplicação;
4 - Divisão.
'''))
if op == 1:
    print(f'{n1} + {n2} = {n1+n2}')
elif op == 2:
    print(f'{n1} - {n2} = {n1-n2}')
elif op == 3:
    print(f'{n1} x {n2} = {n1*n2}')
elif op == 4:
    print(f'{n1} ÷ {n2} = {n1/n2}')
else:
    print('Operação inválida.')
