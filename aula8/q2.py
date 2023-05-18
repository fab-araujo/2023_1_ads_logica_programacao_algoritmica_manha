numero = input("Digite um número: ")
numero = float(numero)

maior_numero = numero

contador = 2

while contador <= 5:
    numero = input("Digite um número: ")
    numero = float(numero)
    if numero > maior_numero:
        maior_numero = numero
    contador = contador + 1

print(maior_numero)