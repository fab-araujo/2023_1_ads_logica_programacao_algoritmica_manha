val_hora = input("Digite o valor da sua hora: ")
val_hora = float(val_hora)

total_horas = input("Quantas horas você trabalhou no mês? ")
total_horas = float(total_horas)

salario_bruto = val_hora * total_horas

if salario_bruto <= 900:
    desconto_ir = 0
    valor_ir = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto_ir = 5/100 * salario_bruto
    valor_ir = 5
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir = 10/100 * salario_bruto
    valor_ir = 10
else:
    desconto_ir = 20/100 * salario_bruto
    valor_ir = 20

desconto_sind = 3/100 * salario_bruto
desconto_inss = 10/100 * salario_bruto
fgts = 11/100 * salario_bruto

salario_liquido = salario_bruto - desconto_inss - desconto_ir - desconto_sind

print("Salaário bruto: R$"+str(salario_bruto))
print("(-) IR ("+str(valor_ir)+"%): R$"+str(desconto_ir))
print("(-) Desconto sindicato: R$"+str(desconto_sind))
print("(-) Desconto INSS (10%): R$"+str(desconto_inss))
print("FGTS (11%): R$"+str(fgts))
print("Salaário líquido: R$"+str(salario_liquido))