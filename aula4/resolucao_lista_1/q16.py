"""
16.	Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math
metragem = input("Qual o valor de metros quadrados que você deseja pintar? ")
metragem = float(metragem)

litros = metragem / 3
latas = litros / 18
latas = math.ceil(latas)
valor = latas * 80
valor = round(valor,2)

latas = str(latas)
valor = str(valor)

print("Você precisa de "+latas+" latas de tintas")
print("O valor total é: R$"+valor)