def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        print("Depósito realizado com sucesso!")
        return saldo, f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, ""

def sacar(saldo, valor, numero_saques, LIMITE_SAQUES, limite):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        numero_saques += 1
        print("Saque realizado com sucesso!")
        return saldo, f"Saque: R$ {valor:.2f}\n", numero_saques
    return saldo, "", numero_saques

def exibir_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    print(extrato or "Não foram realizadas movimentações.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================")

# Loop principal
def main():
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu).lower()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, deposito = depositar(saldo, valor)
            extrato += deposito
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, saque, numero_saques = sacar(saldo, valor, numero_saques, LIMITE_SAQUES, limite)
            extrato += saque
        elif opcao == "e":
            exibir_extrato(extrato, saldo)
        elif opcao == "q":
            print("Obrigado por usar nosso sistema bancário!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()