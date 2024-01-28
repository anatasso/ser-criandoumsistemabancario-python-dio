def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:         R$ {valor:7.2f} +\n'
    else:
        print('Valor informado para depósito é inválido.')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_por_saque, numero_saques, limite_saques_diarios):
    excedeu_limite_saques = numero_saques >= limite_saques_diarios
    excedeu_limite_por_saque = valor > limite_por_saque
    excedeu_saldo = valor > saldo

    if excedeu_limite_saques:
        print('Limite de saques excedido.')
    elif excedeu_limite_por_saque:
        print('Limite por saque excedido.')
    elif excedeu_saldo:
        print('Não será possível sacar o dinheiro por falta de saldo.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:            R$ {valor:7.2f} -\n'
        numero_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print('Valor informado para saque é inválido.')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(' EXTRATO '.center(28,'='))
    if extrato:
        print(extrato.rstrip('\n'))
        print('========='.center(28,'='))
    print(f'Saldo:            R$ {saldo:7.2f} =')
    print('========='.center(28,'='))

def filtrar_cliente(clientes):
    cpf = input('CPF: ')
    cpf = cpf.replace('.','').replace('-','')

    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return True, cpf

    return False, cpf          

def cadastrar_cliente(clientes):
    cliente_cadastrado, cpf = filtrar_cliente(clientes)

    if not cliente_cadastrado:
        nome = input('Nome: ')
        data_nascimento = input('Data de nascimento: ')
        endereco = input('Endereço: ')
        cliente = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}
        clientes.append(cliente)
        print(clientes)
    else:
        print('Cliente já está cadastrado.')

def abrir_conta(clientes, contas_bancarias):
    cliente_cadastrado, cpf = filtrar_cliente(clientes)

    if cliente_cadastrado:
        numero_conta = len(contas_bancarias) + 1
        nova_conta = {'agencia': '0001', 'numero_conta': numero_conta, 'cpf': cpf}
        contas_bancarias.append(nova_conta)
        print(contas_bancarias)
    else:
        print('Cadastre o cliente.')

clientes = []
contas_bancarias = []
saldo = 0
LIMITE_POR_SAQUE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3
menu = '''
===== MENU =====
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[c] Nova conta
[q] Sair

=> '''

while True:
    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Informe o valor de depósito: '))
        saldo, extrato = depositar(saldo, deposito, extrato)

    elif opcao == 's':
        saque = float(input('Informe o valor do saque: '))
        saldo, extrato = sacar(saldo=saldo, valor=saque, extrato=extrato, limite_por_saque=LIMITE_POR_SAQUE, numero_saques=numero_saques, limite_saques_diarios=LIMITE_SAQUES_DIARIOS)

    elif opcao == 'e':
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'u':
        cadastrar_cliente(clientes)

    elif opcao == 'c':
        abrir_conta(clientes, contas_bancarias)
    
    elif opcao == 'q':
        print('Volte sempre.')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')           