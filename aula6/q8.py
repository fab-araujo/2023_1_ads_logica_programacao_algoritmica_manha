salario = input("Digite o salário para ser reajustado: ")
salario = float(salario)

if salario <= 280:
    percentual = 20/100
elif salario > 280 and salario <= 700:
    percentual = 15/100
elif salario > 700 and salario <= 1500:
    percentual = 10/100
else:
    percentual = 5/100

valor_aumento = salario * percentual
novo_salario = salario + valor_aumento

print("O valor do salário antes do reajuste é: R$"+str(salario))
print("O percentual de reajuste aplicado foi: "+str(percentual*100)+"%")
print("O aumento foi de: R$"+str(valor_aumento))
print("O novo salário depois do reajuste é: R$"+str(novo_salario))