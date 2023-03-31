ano = input("Digite o ano: ")
ano = int(ano)

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
    print("É bissexto")
else:
    print("Não é bissexto")