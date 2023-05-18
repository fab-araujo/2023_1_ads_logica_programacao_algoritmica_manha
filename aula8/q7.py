n = input("Digite o número que você quer ver a tabuada: ")
n = int(n)

contador = 1
print("Tabuada de "+str(n)+":")
while contador <= 10:
    resultado = contador * n
    print(str(n)+" x "+str(contador)+" = "+str(resultado))
    contador = contador + 1