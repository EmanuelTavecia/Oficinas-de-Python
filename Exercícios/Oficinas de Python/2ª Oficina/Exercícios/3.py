# EXERCÍCIO 3:

# Crie um programa que leia a idade de uma pessoa.
# Se a idade for maior ou igual a 18, o programa deverá
# exibir a mensagem “Você já é maior de idade!”,
# caso contrário, exibirá “Você ainda é menor de idade.”

# Resolução:

idade = int(input('Qual sua idade? '))
if idade >= 18:
    print('Você já é maior de idade!')
else:
    print('Você ainda é menor de idade.')