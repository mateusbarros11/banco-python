import os

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

saldo = 0
extrato_movimentacoes = []

def menu():
    while True:

        limpar_tela()

        print(f"Bem-vindo, {nome}.\n")

        print("===== MENU =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Ver extrato")
        print("5 - Fazer PIX")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        limpar_tela()

        match opcao:

            case "1":
                depositar()

            case "2":
                sacar()

            case "3":
                consultar_saldo()

            case "4":
                extrato()

            case "5":
                pix()

            case "6":
                sair()

            case _:
                print("Opção inválida.")

def depositar():
    global saldo

    while True:

        print(f"Seu saldo é de R${saldo:.2f}.")
        try:
            valordep = float(input("Digite o valor que deseja depositar: "))
        except ValueError:
            limpar_tela()
            print("Digite apenas números.")
            continue

        if valordep > 0:
            saldo += valordep
            print(f'Depósito realizado com sucesso. Seu saldo é de R${saldo:.2f}')
            extrato_movimentacoes.append(f'Depósito: R${valordep:.2f}')

            while True:

                escolhadep = input("Gostaria de fazer outro depósito? (S/N): ")

                if escolhadep.upper() == "N" :
                    return

                elif escolhadep.upper() == "S":
                    break

                else:
                    print('Opção inválida!')

        else:
            print("Digite um número válido!")

def sacar():
    global saldo

    while True:

        print(f"Seu saldo é de R${saldo:.2f}.")
        
        try:
            valorsaque = float(input("Digite o valor que deseja sacar: "))
        except ValueError:
            limpar_tela()
            print("Digite apenas números.")
            continue

        if valorsaque <= 0:
            print("Valor inválido.")
            continue

        elif valorsaque > saldo:
            print("Saldo insuficiente.")
            continue

        else:
            saldo = saldo - valorsaque
            print(f"Saque realizado com sucesso. Seu saldo atual é de R${saldo:.2f}.")
            extrato_movimentacoes.append(f"Saque: R${valorsaque:.2f}")

            while True:

                escolhasaque = input("Gostaria de realizar outro saque? (S/N): ")

                if escolhasaque.upper() == "N":
                    return

                elif escolhasaque.upper() == "S":
                    break

                else:
                    print("Resposta inválida. Escolha a opção adequada.")

def consultar_saldo():

    print(f"Seu saldo atual é de R${saldo:.2f}")

    while True:

        escolhasaldo = input("Para voltar ao menu principal, digite M: ")
        if escolhasaldo.upper() == "M":
            return

        else:
            limpar_tela()
            print("Opção inválida. Tente novamente!")
            continue

def extrato():

    while True:

        if not extrato_movimentacoes:
            print("Não foram realizadas movimentações.")               
            escolha_extrato = input('Para voltar ao menu principal, digite "M": ')

            if escolha_extrato.upper() == "M":
                return

            else:
                limpar_tela()
                print("Opção inválida.")
                continue

        else:
            for item in extrato_movimentacoes:
                print(item)
            escolha_extrato = input('Para voltar ao Menu principal, digite "M": ')
            
            if escolha_extrato.upper() == "M":
                limpar_tela()
                return

            else:
                limpar_tela()
                print("Opção inválida.")
                continue

def pix():
    global saldo

    while True:

        chave = input("Digite a chave PIX: ")
        try:
            valorpix = float(input("Digite o valor: "))
        except ValueError:
            limpar_tela()
            print("Digite apenas números.")
            continue

        if valorpix <= 0:
            print("Valor inválido.")
            continue

        elif valorpix > saldo:
            print("Saldo insuficiente.")
            continue

        else:
            saldo = saldo - valorpix
            print("Transferência realizada com sucesso.")
            print(f"Seu saldo atualizado é de R${saldo:.2f}")
            extrato_movimentacoes.append(f"PIX enviado para a chave {chave}: R${valorpix:.2f}")

            while True:

                escolhapix = input("Gostaria de realizar outra transferência PIX? (S/N): ")

                if escolhapix.upper() == "S":
                    break

                elif escolhapix.upper() == "N":
                    return

                else:
                    print("Opção inválida.")

def sair():

    print("Até mais!")
    exit()

nome = input('Digite seu nome: ')
email = input('Digite o seu email: ')
senha = input('Digite sua senha: ')
menu()