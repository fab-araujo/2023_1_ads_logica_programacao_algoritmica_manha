sal_inicial = input("Digite o salário inicial: ")
sal_inicial = float(sal_inicial)
aumento_percentual = 1.5/100
aumento = aumento_percentual * sal_inicial

salario = sal_inicial + aumento

contador = 1997

while contador < 2000:
    aumento_percentual = aumento_percentual * 2
    aumento = aumento_percentual * salario
    salario = salario + aumento
    contador = contador + 1

print(salario)