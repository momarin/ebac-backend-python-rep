# Lista

flores = ["rosa", "margarida", "violeta", "crisântemo", "girassol", "orquídea"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Guardando cópias originais
flores_original = flores.copy()
numeros_original = numeros.copy()

# Adicionando mais flores
flores.append("lírio")
numeros.extend([10, 11, 12])

# Exibindo originais
print("Listas originais:")
print(f"Flores: {flores_original}")
print(f"Números: {numeros_original}")

# Exibindo atualizados
print("\nListas com append:")
print(f"Flores: {flores}")
print(f"Números: {numeros}")

# Flores que contém a letra L
print("\nFlores que contém a letra L:")
for flor in flores:
    if "l" in flor:
        print(flor)

# Apenas números primos
print("\nNúmeros primos:")
for numero in numeros:
    if numero > 1:
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False  
                break
        if primo:
            print(numero)