a = 1
b = 1

contador = 3
numero_serie = 0

while numero_serie <= 500:
    numero_serie = a + b
    print(numero_serie)
    a = b
    b = numero_serie
    contador = contador + 1

print(numero_serie)