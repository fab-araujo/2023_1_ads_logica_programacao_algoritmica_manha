total_pares = 0
total_impares = 0

contador = 1

while contador <= 10:
    numero = input("Digite um número: ")
    numero = int(numero)
    if numero % 2 == 0:
        total_pares = total_pares + 1
    else:
        total_impares = total_impares + 1
    
    contador = contador + 1

print(total_pares)
print(total_impares)