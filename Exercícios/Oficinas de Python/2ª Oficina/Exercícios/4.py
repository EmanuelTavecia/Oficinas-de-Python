# EXERCÍCIO 4:

# Crie um programa que peça uma senha para entrar no sistema.
# A senha válida será o número 1234. Se a senha digitada for válida,
# o programa deverá exibir a mensagem “Acesso autorizado”,
# mas se a senha for inválida, exibirá “Acesso negado”.

# Resolução:

senha = int(input('Digite a senha para entrar no sistema: '))
if senha == 1234:
    print('Acesso autorizado.')
else:
    print('Acesso negado.')