codigos = []
alturas = []

codigo = 1

while codigo != "0":
    codigo = input("Digite o seu código: ")
    if codigo!= "0":
        codigos.append(codigo)

        altura = input("Digite a sua altura: ")
        altura = float(altura)
        alturas.append(altura)


cod_mais_alto = codigos[0]
valor_mais_alto = alturas[0]
cod_mais_baixo = codigos[0]
valor_mais_baixo = alturas[0]

index = 0

while index < len(codigos):
    if alturas[index] > valor_mais_alto:
        valor_mais_alto = alturas[index]
        cod_mais_alto = codigos[index]

    if alturas[index] < valor_mais_baixo:
        valor_mais_baixo = alturas[index]
        cod_mais_baixo = codigos[index]

    index = index + 1

print(cod_mais_alto+" é o mais alto com "+str(valor_mais_alto))
print(cod_mais_baixo+" é o mais baixo com "+str(valor_mais_baixo))