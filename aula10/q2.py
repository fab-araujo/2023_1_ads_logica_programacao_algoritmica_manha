def imprimeN(n):
    inicio = 1
    while inicio <= n:
        repet = 1
        while repet <= inicio:
            print(repet, end=" ")
            repet = repet + 1
        print("")
        inicio = inicio + 1

num = input("Digite um número maior ou igual a 1: ")
num = int(num)
imprimeN(num)