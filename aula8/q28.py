n = input("Digite quantos elementos você quer: ")
n = int(n)

l = []

for i in range(n):
    aux = input("Digite uma temperatura: ")
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
print(soma/len(l))