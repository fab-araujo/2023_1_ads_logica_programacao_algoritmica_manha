n1 = input("Digite um número: ")
n1 = int(n1)
n2 = input("Digite um número: ")
n2 = int(n2)

soma = 0
contador = n1
contador = contador + 1

while contador > n1 and contador < n2:
    print(contador)
    soma = soma + contador
    contador = contador + 1

print(soma)