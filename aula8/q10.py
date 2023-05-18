n = input("Digite um número: ")
n = int(n)
a = 1
b = 1

contador = 3

while contador <= n:
    numero_serie = a + b
    a = b
    b = numero_serie
    contador = contador + 1

print(numero_serie)