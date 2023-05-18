n = input("Digite o valor: ")
n = int(n)

h = 1

contador = 2

while contador <= n:
    h = h + (1/contador)
    contador = contador + 1

print(h)