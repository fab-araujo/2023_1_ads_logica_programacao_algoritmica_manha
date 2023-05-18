def somatoria(n):
    soma = 0
    for i in range(n+1):
        soma = soma + i
    return soma

n = input("Digite um número: ")
n = int(n)
soma = somatoria(n)
print("A somatória de todos os número de 0 até "+str(n)+" é: "+str(soma))
