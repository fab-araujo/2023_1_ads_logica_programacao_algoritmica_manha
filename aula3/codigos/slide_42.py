#slide42
anos = input("Digite os anos da sua idade: ")
i_anos = int(anos)

meses = input("Digite os meses da sua idade: ")
i_meses = int(meses)

dias = input("Digite os dias da sua idade: ")
i_dias = int(dias)

total_dias = (i_anos * 365) + (i_meses * 30) + i_dias
s_total_dias = str(total_dias)

print("Sua idade em dias é: "+s_total_dias)