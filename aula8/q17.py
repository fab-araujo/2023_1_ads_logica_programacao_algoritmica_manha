n = input("Digite um número: ")
n = int(n)

contador = 2
primo = True
div = []

while contador < n:
    if n % contador == 0:
        primo = False
        div.append(contador)
    contador = contador + 1

print(primo)
if len(div) > 0:
    print(div)