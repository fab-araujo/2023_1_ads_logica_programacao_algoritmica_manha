"""
9.	Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. Use a fórmula: C = 5 * ((F-32) / 9).
"""
temperatura_f = input("Digite a temparatura em Fahrenheit: ")
temperatura_f = float(temperatura_f)
conversao_c = 5 * ((temperatura_f - 32) / 9)
conversao_c = round(conversao_c, 2)
print(conversao_c)