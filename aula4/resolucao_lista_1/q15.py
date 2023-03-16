"""
15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
o	salário bruto.
o	quanto pagou ao INSS.
o	quanto pagou ao sindicato.
o	o salário líquido.
o	calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
valor_hora = input("Digite quanto você ganha por hora: ")
valor_hora = float(valor_hora)
horas = input("Digite quantas horas você trabalhou: ")
horas = int(horas)

salario_bruto = valor_hora * horas
salario_bruto = round(salario_bruto,2)
ir = salario_bruto * 0.11
ir = round(ir,2)
inss = salario_bruto * 0.08
inss = round(inss,2)
sindicato = salario_bruto * 0.05
sindicato = round(sindicato,2)

salario_liquido = salario_bruto - ir - inss - sindicato

salario_bruto = str(salario_bruto)
ir = str(ir)
inss = str(inss)
sindicato = str(sindicato)
salario_liquido = str(salario_liquido)

print("+ Salário Bruto : R$"+salario_bruto)
print("- IR (11%) : R$"+ir)
print("- INSS (8%) : R$"+inss)
print("- Sindicato (5%) : R$"+sindicato)
print("= Salário Liquido : R$"+salario_liquido)
