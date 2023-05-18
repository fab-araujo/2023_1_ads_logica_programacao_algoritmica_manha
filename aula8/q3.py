numero = input("Digite um número: ")
numero = float(numero)

contador = 2

soma = numero

while contador <= 5:
    numero = input("Digite um número: ")
    numero = float(numero)
    soma = soma + numero

    contador = contador + 1

print(soma)
print(soma/5)