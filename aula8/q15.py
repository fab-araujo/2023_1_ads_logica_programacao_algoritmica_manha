contador = 0

while contador == 0:
    n = input("Digite um número: ")
    n = int(n)
    while n <= 0 or n > 15:
        print("Número inválido!")
        n = input("Digite um número: ")
        n = int(n)

    fatorial = 1

    contador = n

    while contador >= 1:
        fatorial = fatorial * contador
        contador = contador - 1

    print(fatorial)