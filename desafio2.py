import textwrap

def menu():

    menu = """\n

    -------- BEM-VINDO ---------

    [1] - DEPOSITAR
    [2] - SACAR
    [3] - EXTRATO
    [4] - NOVO USUÁRIO
    [5] - CRIAR NOVA CONTA
    [6] - LISTAR CONTAS
    [7] - SAIR

    ----------------------------
      DIGITE A OPÇÃO DESEJADA:

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("--------------------------------------------")
        print(f"Depósito realizado no valor de R${valor}")
        print("--------------------------------------------")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo para executar esta operação!")

    elif excedeu_limite:
        print("Você não tem limite para executar esta operação!")

    elif excedeu_saques:
        print("Número máximo de saques atingidos, tente novamente amanhã!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("--------------------------------------")
        print(f"Saque realizado no valor de R${valor:.2f}")
        print("--------------------------------------")

    else:
        print("----------------------------------------------")
        print("Operação falhou! O valor informado é inválido.")
        print("----------------------------------------------")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("-------- EXTRATO -----------")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("----------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números, sem pontuação):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Falha! Já existe usuário cadastrado no CPF informado!")
        return

    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe aqui o endereço completo (rua, número, bairro, cidade, sigla do estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("-------------------------------------")
    print("Parabéns! Usuário criado com sucesso!")
    print("-------------------------------------")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números, sem pontuação):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("----------------------------------")
        print("Parabéns!Conta criada com sucesso!")
        print("----------------------------------")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Falha! Usuário não encontrado...encerrando operação!")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\ 
Agência:\t{conta['agencia']}
C/C:\t\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
"""
        print("=" * 50)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor a ser depositado:"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor desejado:"))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_nova_conta(AGENCIA, numero_conta, usuarios)

            if  conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("--------------------------------")
            print("Opção inválida. Tente novamente.")
            print("--------------------------------")

main()




