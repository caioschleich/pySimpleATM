saldoConta = 0
limiteSaque = 500
extrato = ""
numeroSaques = 0
countSaques = 3

menu = """
Olá! Esse é o sistema do ATM. Aqui você pode:

[s] Sacar
[d] Depositar
[e] Ver Extrato
[x] Sair

Digite o código da função desejada ==> """

while True:
    codigo = input(menu)

    if codigo == "s":
        print("Você selecionou: Sacar")
        valorSaque = float(input("Digite o valor que deseja sacar: "))
        excedeSaldo = valorSaque > saldoConta
        excedeLimite = valorSaque > limiteSaque
        excedeSaques = numeroSaques >= countSaques

        if excedeSaldo:
            print("Ops! Você não tem saldo suficiente, tente novamente.")

        elif excedeLimite:
            print("Ops! O valor excede seu limite diário, tente novamente.")

        elif excedeSaques:
            print("Ops! Você só pode realizar 3 saques diários, tente novamente amanhã.")

        elif valorSaque > 0:
            print(f"Sucesso! Você sacou R$ {valorSaque:.2f}")
            saldoConta -= valorSaque
            extrato += f"Saque: R$ {valorSaque:.2f}\n"
            numeroSaques += 1

        else:
            print("Valor inválido! Tente novamente")

    elif codigo == "d":
        print("Você selecionou: Depositar")
        valorDeposito = float(input("Digite o valor que deseja depositar: "))
        if valorDeposito > 0:
            saldoConta += valorDeposito
            extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
            print(f"Sucesso! Você depositou R$ {valorDeposito:.2f}")
        else:
            print("Valor inválido! Operação encerrada")
            break

    elif codigo == "e":
        print("Você selecionou: Extrato")
        print(f"Você possui R$ {saldoConta:.2f} na sua conta.")
        print(extrato)

    elif codigo == "x":
        print("Agradecemos e volte sempre!")
        break

    else:
        print("Operação inválida, selecione o código desejado e tente novamente.")