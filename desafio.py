"""Sistema bancário simples — desafio da formação Python da DIO.

Operações: depósito, saque e extrato.
Regras:
  - depósitos só com valores positivos;
  - no máximo 3 saques por dia, de até R$ 500,00 cada;
  - saque só se houver saldo;
  - o extrato lista todas as movimentações e o saldo atual.
"""

MENU = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500.0


def ler_valor(mensagem):
    """Pede um valor em reais. Aceita vírgula ou ponto; devolve None se for inválido."""
    texto = input(mensagem).strip().replace(",", ".")
    try:
        return float(texto)
    except ValueError:
        return None


def depositar(saldo, valor, extrato, /):
    if valor is None or valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

    saldo += valor
    extrato.append(f"Depósito:\tR$ {valor:.2f}")
    print("Depósito realizado com sucesso!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, numero_saques):
    if valor is None or valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > LIMITE_POR_SAQUE:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {LIMITE_POR_SAQUE:.2f}.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques diários excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque:\t\tR$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("\n".join(extrato) if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def main():
    saldo = 0.0
    extrato = []
    numero_saques = 0

    while True:
        opcao = input(MENU).strip().lower()

        if opcao == "d":
            valor = ler_valor("Informe o valor do depósito: ")
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = ler_valor("Informe o valor do saque: ")
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                numero_saques=numero_saques,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Obrigado por usar o sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
