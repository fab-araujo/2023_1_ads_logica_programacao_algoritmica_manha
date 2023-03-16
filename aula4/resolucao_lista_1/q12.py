"""
12.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = input("Digite a sua altura: ")
altura = float(altura)

peso_ideal = (72.7 * altura) - 58
print(peso_ideal)