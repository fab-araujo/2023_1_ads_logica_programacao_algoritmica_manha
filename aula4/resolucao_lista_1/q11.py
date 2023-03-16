"""
11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o	o produto do dobro do primeiro com metade do segundo.
o	a soma do triplo do primeiro com o terceiro.
o	o terceiro elevado ao cubo.
"""
x = input("Digite um número inteiro: ")
x = int(x)
y = input("Digite um número inteiro: ")
y = int(y)
z = input("Digite um número real: ")
z = float(z)

exp1 = (2 * x) * (y / 2)
print(exp1)

exp2 = (3 * x) + z
print(exp2)

exp3 = z ** 3
print(exp3)