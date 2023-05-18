eleitores = input("Quantos eleitores existem? ")
eleitores = int(eleitores)

votosA = 0
votosB = 0
votosC = 0

contador = 1

while contador <= eleitores:
    voto = input("Qual candidato você vota: A, B ou C?")
    if voto == "A":
        votosA = votosA + 1
    elif voto == "B":
        votosB = votosB + 1
    elif voto == "C":
        votosC = votosC + 1
    else:
        print("Você anulou seu voto.")
    
    contador = contador + 1

print(votosA)
print(votosB)
print(votosC)