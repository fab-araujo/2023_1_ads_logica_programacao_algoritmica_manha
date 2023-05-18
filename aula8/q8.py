base = input("Digite a base: ")
base = int(base)
expoente = input("Digite o expoente: ")
expoente = int(expoente)

contador = 1
resultado = 1

while contador <= expoente:
    resultado = resultado * base
    contador = contador + 1

print(resultado)