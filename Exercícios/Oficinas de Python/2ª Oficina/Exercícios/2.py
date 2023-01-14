# EXERCÍCIO 2:

# Crie um programa que peça duas notas de um aluno.
# O programa fará a média aritmética entre as notas
# e caso seja igual a 10, será exibido a mensagem “Aprovado com nota máxima”,
# caso seja maior ou igual a 6, exibirá “Aprovado com média x”
# e caso a média for menor que 6, exibirá “Reprovado com média y”.

# Resolução:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m == 10:
    print('Aprovado com nota máxima.')
elif m >= 6:
    print(f'Aprovado com média {m}')
else:
    print(f'Reprovado com média {m}')