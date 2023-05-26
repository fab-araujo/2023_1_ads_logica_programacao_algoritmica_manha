def dozePara24 (hora, minuto):
    horaConvertida = hora
    aOuP = "A"
    if hora > 12:
        horaConvertida = hora - 12
        aOuP = "P"
    return [str(horaConvertida) + ":" + str(minuto), aOuP]

def printHora(hora, minuto):
    horaMinCon = dozePara24(hora, minuto)
    if horaMinCon[1] == "P":
        print(horaMinCon[0] + " P.M")
    else:
        print(horaMinCon[0] + " A.M")

hora = ""
while hora != "X":
    hora = input("Digite uma hora ou 'X' para sair: ")
    if hora != "X":
        minuto = input("Digite um minuto: ")
        hora = int(hora)
        minuto = int(minuto)
        printHora(hora, minuto)