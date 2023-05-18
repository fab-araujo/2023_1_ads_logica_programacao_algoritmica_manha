n = input("Quantas notas você deseja? ")
n = int(n)
soma = 0

for i in range(n):
    nota = input("Digite uma nota: ")
    nota = float(nota)
    soma = soma + nota

print(soma/n)