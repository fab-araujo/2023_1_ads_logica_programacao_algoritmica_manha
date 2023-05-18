n = input("Digite um número: ")
n = int(n)

fatorial = 1

contador = n

while contador >= 1:
    fatorial = fatorial * contador
    contador = contador - 1

print(fatorial)