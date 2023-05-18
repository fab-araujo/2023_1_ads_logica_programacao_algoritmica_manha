n = input("Digite um número: ")
n = int(n)

contador = 2
primo = True

while contador < n:
    if n % contador == 0:
        primo = False
    contador = contador + 1

print(primo)