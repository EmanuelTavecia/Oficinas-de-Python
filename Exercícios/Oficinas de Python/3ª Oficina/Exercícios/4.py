# EXERCÍCIO 4:

# Faça um programa que simule um Caixa Eletrônico.
# O usuário poderá DEPOSITAR, SACAR e CONSULTAR SALDO da conta bancária.
# O programa deverá apresentar as opções na tela e perguntar ao usuário qual ele quer:
# 1 - Sacar; 2 – Depositar; 3 - Consultar Saldo; 4 - Encerrar.
# Se o usuário escolher 1 (SACAR), o programa deverá perguntar qual o valor a ser sacado.
# Então, deverá verificar se há saldo suficiente para sacar.
# Se sim, debita o valor da conta e informe: "SAQUE REALIZADO COM SUCESSO!".
# Se não, informa: "SALDO INSUFICIENTE".
# Se o usuário escolher 2 (DEPOSITAR), o programa deverá perguntar qual o valor a ser depositado.
# Então, deverá adicionar o valor informado pelo usuário ao saldo da conta
# e informar: "DEPÓSITO REALIZADO COM SUCESSO!".
# Se o usuário escolher 3 (CONSULTAR SALDO), o programa deverá mostrar uma mensagem
# informando o saldo atual da conta bancária.
# O programa só encerra, se o usuário digitar 4 (ENCERRAR).
# Se a opção for diferente de 1, 2, 3 e 4,
# uma mensagem deverá ser mostrada ao usuário informando OPÇÃO INVÁLIDA.
# A cada mensagem exibida, deve-se ter um delay (pausa) de 2 segundos.

# Resolução:

import time

saldo = 2683.75
op = int(input('''1 - Sacar;
2 – Depositar;
3 - Consultar Saldo;
4 - Encerrar.
'''))
while op != 4:
    if op == 1:
        saque = float(input('Qual o valor a ser sacado? R$'))
        if saldo >= saque:
            saldo -= saque
            print('Saque realizado com sucesso!')
            print(f'Seu saldo atual é de R${saldo}')
            time.sleep(2)
        else:
            print('Saldo insuficiente.')
            time.sleep(2)
    elif op == 2:
        deposito = float(input('Qual o valor a ser depositado? R$'))
        saldo += deposito
        print('Depósito realizado com sucesso!')
        print(f'Seu saldo é de R${saldo}')
        time.sleep(2)
    elif op == 3:
        print(f'Seu saldo é de R${saldo}')
        time.sleep(2)
    else:
        print('Opção inválida.')
        time.sleep(2)
    op = int(input('''1 - Sacar;
2 – Depositar;
3 - Consultar Saldo;
4 - Encerrar.
'''))
