# Funções
a = 6
b = 3

# SOMA
def somar(a, b):
    return a + b

# SUBTRAÇÃO
def subtrair(a, b):
    return a - b

# MULTIPLICAÇÃO
def multiplicar(a, b):
    return a * b

# DIVISÃO
def dividir(a, b):
    return a / b

print(f"Numeros calculados: {a} e {b}")

print(f"Soma: {somar(a, b)}")
print(f"Subtração: {subtrair(a, b)}")
print(f"Multiplicação: {multiplicar(a, b)}")
print(f"Divisão: {dividir(a, b)}")

# ---------------------------------------------------
print("\nImprimindo números")
def numeros_aleatorios():
    nums = [3, 5, 2, 7, 9]

    for i in nums:
        print(i)

numeros_aleatorios()
# ---------------------------------------------------
print("\nGerando palavras aleatórias")

def gerador_de_palavras_aleatorias():
    palavras = ["lorem", "ipsum", "dolor"]

    for i in palavras:
        if "l" in i:
            print(i)

gerador_de_palavras_aleatorias()