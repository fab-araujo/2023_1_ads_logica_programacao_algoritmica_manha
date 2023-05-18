parcelas = [1,3,6,9,12]
juros = [0,10,15,20,25]

divida = input("Digite o valor da dívida: ")
divida = float(divida)
total_divida = divida
index = 0

while index < len(parcelas):
    val_juros = divida * juros[index] / 100
    total_divida = divida + val_juros

    print(str(total_divida)+" "+str(val_juros)+" "+str(parcelas[index])+" "+str(total_divida/parcelas[index]))
    
    index = index + 1