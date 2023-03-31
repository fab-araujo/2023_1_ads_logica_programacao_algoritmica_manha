litros = input("Quantos litros você vai abastecer: ")
litros = float(litros)

tipo_combustivel = input("Álcool ou Gasolina? Digite A ou G: ")

if tipo_combustivel == "A":
    if litros < 20:
        desconto = 3/100 * litros
    else:
        desconto = 5/100 * litros

    litros_final = litros - desconto
    valor = litros_final * 1.9
    print("O total a pagar é R$"+str(valor))
else:
    if litros < 20:
        desconto = 4/100 * litros
    else:
        desconto = 6/100 * litros

    litros_final = litros - desconto
    valor = litros_final * 2.5
    print("O total a pagar é R$"+str(valor))