codigos = ["Belem","Ananindeua","Marituba","Castanhal","Mosqueiro"]
n_veiculos = [1000, 2000, 3000, 4000, 5000]
acidentes = [100,200,300,400,500]

cod_mais_acidentes = codigos[0]
valor_mais_acidentes = acidentes[0]
cod_menos_acidentes = codigos[0]
valor_menos_acidentes = acidentes[0]

index = 0

soma_veiculos = 0
soma_acidentes = 0
n_menor_2000 = 0

while index < len(codigos):
    if acidentes[index] > valor_mais_acidentes:
        valor_mais_acidentes = acidentes[index]
        cod_mais_acidentes = codigos[index]

    if acidentes[index] < valor_menos_acidentes:
        valor_menos_acidentes = acidentes[index]
        cod_menos_acidentes = codigos[index]

    soma_veiculos = soma_veiculos + n_veiculos[index]
    if n_veiculos[index] <= 2000:
        soma_acidentes = soma_acidentes + acidentes[index]
        n_menor_2000 = n_menor_2000 + 1

    index = index + 1

print(cod_mais_acidentes+" é o que tem mais acidentes com "+str(valor_mais_acidentes))
print(cod_menos_acidentes+" é o que tem menos acidentes com "+str(valor_menos_acidentes))

print(soma_veiculos / len(codigos))
print(soma_acidentes / n_menor_2000)