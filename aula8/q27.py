n = input("Digite um número: ")
n = int(n)

fatorial = 1

contador = n

print(str(n)+"! = ", end="")

while contador >= 1:
    print(str(contador), end="")
    if contador > 1:
        print(" . ", end="")
    fatorial = fatorial * contador
    contador = contador - 1

print(" = " + str(fatorial))