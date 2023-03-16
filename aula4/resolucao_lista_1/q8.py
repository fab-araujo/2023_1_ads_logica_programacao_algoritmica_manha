"""
8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
valor_hora = input("Quanto você ganha por hora? ")
valor_hora = float(valor_hora)
qtd_horas = input("Quantas horas você trabalha por mês? ")
qtd_horas = int(qtd_horas)
salario = valor_hora * qtd_horas
salario = str(salario)
print("O seu salário é: R$ "+salario)