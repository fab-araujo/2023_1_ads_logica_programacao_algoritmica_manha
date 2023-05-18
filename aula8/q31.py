n = input("Digite o número que você quer ver a tabuada: ")
n = int(n)

inicio = input("Qual número deverá começar: ")
inicio = int(inicio)
fim = input("Qual número deverá terminar: ")
fim = int(fim)

contador = inicio
print("Tabuada de "+str(n)+":")
print("Início: "+str(inicio)+":")
print("Fim: "+str(fim)+":")
while contador <= fim:
    resultado = contador * n
    print(str(n)+" x "+str(contador)+" = "+str(resultado))
    contador = contador + 1