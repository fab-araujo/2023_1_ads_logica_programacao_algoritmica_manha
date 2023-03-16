"""
10.	Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
temperatura_c = input("Digite a temparatura em Cenlsius: ")
temperatura_c = float(temperatura_c)
conversao_f = 1.8 * temperatura_c + 32
conversao_f = round(conversao_f, 2)
print(conversao_f)