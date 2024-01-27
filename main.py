menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
LIMITE_SAQUE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Informe o valor de depósito: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito:         R$ {deposito:7.2f} +\n'
        else:
            print('Valor informado para depósito é inválido.')

    elif opcao == 's':
        saque = float(input('Informe o valor do saque: '))

        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES
        excedeu_limite_por_saque = saque > LIMITE_SAQUE
        excedeu_saldo = saque > saldo

        if excedeu_limite_saques:
            print('Limite de saques excedido.')
        elif excedeu_limite_por_saque:
            print('Limite por saque excedido.')
        elif excedeu_saldo:
            print('Não será possível sacar o dinheiro por falta de saldo.')
        elif saque > 0:
            saldo -= saque
            extrato += f'Saque:            R$ {saque:7.2f} -\n'
            numero_saques += 1
        else:
            print('Valor informado para saque é inválido.')

    elif opcao == 'e':
        print(' EXTRATO '.center(28,'='))
        if extrato:
            print(extrato.rstrip('\n'))
            print('========='.center(28,'='))
        print(f'Saldo:            R$ {saldo:7.2f} =')
        print('========='.center(28,'='))

    elif opcao == 'q':
        print('Volte sempre.')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')