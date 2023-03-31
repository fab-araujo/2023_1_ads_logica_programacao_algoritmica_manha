dia = input("Digite o dia: ")
dia = int(dia)

mes = input("Digite o mês: ")
mes = int(mes)

ano = input("Digite o ano: ")
ano = int(ano)

if (((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia > 0 and dia <= 31)) or (mes == 2 and dia > 0 and dia <= 28) or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia > 0 and dia <= 30))) and ano > 0:
    print("Data válida")
else:
    print("Data inválida")