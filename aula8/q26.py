while True:
    total = 0
    valor = input("Qual o valor do produto: ")
    valor = float(valor)
    while valor != 0:
        total = total + valor
        valor = input("Qual o valor do produto: ")
        valor = float(valor)

    print("Total: "+str(total))
    dinheiro = input("Quanto o cliente lhe deu? ")
    dinheiro = float(dinheiro)
    print("Dinheiro: "+str(dinheiro))
    print("Troco: "+str(dinheiro - total))