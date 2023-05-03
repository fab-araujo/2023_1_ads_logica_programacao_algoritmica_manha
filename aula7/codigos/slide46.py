numeros = []
total_numeros = list(range(5))

for n in total_numeros:
    num = input("Digite um número: ")
    num = int(num)
    numeros.append(num)

menor_numero = numeros[0]

for n in numeros:
    if n < menor_numero:
        menor_numero = n

print(numeros)
print(menor_numero)

