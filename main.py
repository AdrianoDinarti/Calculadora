import math
import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def calculadora():
    print("Bem-vindo à Calculadora!")

    continuar = True
    while continuar:
        clear()
        print("""
Escolha a operação:
1. Adição
2. Subtração
3. Multiplicação
4. Porcentagem
5. Raiz Quadrada
6. Divisão
        """)
        operacao = input("Digite o número da operação desejada: ")

        if operacao in ['1', '2', '3', '4', '6']:
            usuario01 = float(input("Insira o primeiro número: "))
            usuario02 = float(input("Insira o segundo número: "))

        if operacao == "1":
            print(f"Resultado do cálculo é: {usuario01 + usuario02}")

        elif operacao == "2":
            print(f"Resultado do cálculo é: {usuario01 - usuario02}")

        elif operacao == "3":
            print(f"Resultado do cálculo é: {usuario01 * usuario02}")

        elif operacao == "4":
            print(f"Resultado do cálculo é: {(usuario01 * usuario02) / 100}%")

        elif operacao == "5":
            num = float(input("Digite um número: "))
            resultado = math.sqrt(num)
            print(f"Resultado: Raiz quadrada de {num} = {resultado}")

        elif operacao == "6":
            try:
                print(f"Resultado do cálculo é: {usuario01 / usuario02}")
            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")

        else:
            print("Operação inválida. Tente novamente.")

        resposta = input("Deseja realizar outra operação? (s/n): ")
        if resposta.lower() != 's':
            continuar = False

    print("Obrigado por usar a calculadora. Até a próxima!")


calculadora()



