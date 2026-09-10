print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada:")

if opcao not in ("1", "2", "3", "4"):
    print("Opção inexistente. Escolha entre opções 1 a 4")
else:
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    if opcao == "1":
        print("Resultado:", num1 + num2)
    elif opcao == "2":
        print("Resultado:", num1 - num2)
    elif opcao == "3":
        print("Resultado", num1 * num2)
    elif opcao == "4":
        print("Resultado", num1 / num2)