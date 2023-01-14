# EXERCÍCIO 11:

# Crie um programa que peça uma nota de zero a dez.
# Se o valor for inválido, mostre uma mensagem de erro.
# O programa só encerra quando o usuário digitar um valor válido.

# Resolução:

nota = int(input('Digite uma nota de zero a dez: '))
while nota < 0 or nota > 10:
    print('Nota inválida.')
    nota = int(input('Digite uma nota de zero a dez: '))
print('Obrigado!')