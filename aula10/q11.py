def dataExtenso(dia, mes, ano):
    meses = [
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro"
    ]
    if dia > 0 and dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return str(dia) + " de " + meses[mes-1] + " de " + str(ano)
    elif dia > 0 and dia <= 28 and mes == 2:
        return str(dia) + " de " + meses[mes-1] + " de " + str(ano)
    elif dia > 0 and dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        return str(dia) + " de " + meses[mes-1] + " de " + str(ano)
    else:
        return "Data inválida"
    
dia = input("Digite um dia: ")
dia = int(dia)
mes = input("Digite um mês: ")
mes = int(mes)
ano = input("Digite um ano: ")
ano = int(ano)
data = dataExtenso(dia, mes, ano)
print(data)
    
