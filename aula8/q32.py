codigos = []
alturas = []
pesos = []

codigo = 1

while codigo != "0":
    codigo = input("Digite o seu código: ")
    if codigo!= "0":
        codigos.append(codigo)

        altura = input("Digite a sua altura: ")
        altura = float(altura)
        alturas.append(altura)

        peso = input("Digite o seu peso: ")
        peso = float(peso)
        pesos.append(peso)


cod_mais_alto = codigos[0]
valor_mais_alto = alturas[0]
cod_mais_baixo = codigos[0]
valor_mais_baixo = alturas[0]
cod_mais_gordo = codigos[0]
valor_mais_gordo = pesos[0]
cod_mais_magro = codigos[0]
valor_mais_magro = pesos[0]

index = 0

soma_pesos = 0
soma_alturas = 0

while index < len(codigos):
    if alturas[index] > valor_mais_alto:
        valor_mais_alto = alturas[index]
        cod_mais_alto = codigos[index]

    if alturas[index] < valor_mais_baixo:
        valor_mais_baixo = alturas[index]
        cod_mais_baixo = codigos[index]

    if pesos[index] > valor_mais_gordo:
        valor_mais_gordo = pesos[index]
        cod_mais_gordo = codigos[index]

    if pesos[index] < valor_mais_magro:
        valor_mais_magro = pesos[index]
        cod_mais_magro = codigos[index]

    soma_pesos = soma_pesos + pesos[index]
    soma_alturas = soma_alturas + alturas[index]

    index = index + 1

print(cod_mais_alto+" é o mais alto com "+str(valor_mais_alto))
print(cod_mais_baixo+" é o mais baixo com "+str(valor_mais_baixo))
print(cod_mais_gordo+" é o mais gordo com "+str(valor_mais_gordo))
print(cod_mais_magro+" é o mais magro com "+str(valor_mais_magro))

print(soma_alturas / len(codigos))
print(soma_pesos / len(codigos))