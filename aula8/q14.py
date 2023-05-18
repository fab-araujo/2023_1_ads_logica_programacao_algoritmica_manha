n = input("Digite quantos elementos você quer: ")
n = int(n)

l = []

for i in range(n):
    aux = input("Digite um número: ")
    aux = float(aux)
    while aux < 0 or aux > 1000:
        print("O valor é inválido! Digite entre 0 e 1000!")
        aux = input("Digite um número: ")
        aux = float(aux)
    l.append(aux)

menor = l[0]
maior = l[0]
soma = 0

for i in l:
    if i > maior:
        maior = i
    
    if i < menor:
        menor = i

    soma = soma + i

print(maior)
print(menor)
print(soma)