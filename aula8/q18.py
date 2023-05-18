n = input("Digite um número: ")
n = int(n)

aux = 2

div = 0

while aux <= n:
    contador = 2
    primo = True

    while contador < aux:
        if aux % contador == 0:
            primo = False
        contador = contador + 1
        div = div + 1

    print(str(aux) + ": ", str(primo))
    aux = aux + 1

print(div)