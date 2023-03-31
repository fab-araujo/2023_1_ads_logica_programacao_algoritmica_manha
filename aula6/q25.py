kg_file_duplo = input("Quantos kilos de filé duplo você vai comprar? ")
kg_file_duplo = int(kg_file_duplo)

kg_alcatra = input("Quantos kilos de alcatra você vai comprar? ")
kg_alcatra = int(kg_alcatra)

kg_picanha = input("Quantos kilos de picanha você vai comprar? ")
kg_picanha = int(kg_picanha)

if ((kg_file_duplo > 0 and (kg_alcatra > 0 or kg_picanha > 0)) or (kg_alcatra > 0 and (kg_file_duplo > 0 or kg_picanha > 0)) or (kg_picanha > 0 and (kg_alcatra > 0 or kg_file_duplo > 0))):
    print("Você só pode escolher um tipo de carne na promoção!")
else:
    cartao_tabajara = input("Você vai pagar no cartão tabajara? Sim ou Não: ")
    total = 0

    if kg_file_duplo > 0 and kg_file_duplo < 5:
        total = total + (kg_file_duplo * 4.9)
    else:
        total = total + (kg_file_duplo * 5.8)

    if kg_alcatra > 0 and kg_alcatra < 5:
        total = total + (kg_alcatra * 5.9)
    else:
        total = total + (kg_alcatra * 6.8)

    if kg_picanha > 0 and kg_picanha < 5:
        total = total + (kg_picanha * 6.9)
    else:
        total = total + (kg_picanha * 7.8)

    if kg_file_duplo > 0:
        print("Tipo de carne: Filé duplo")
        print("Quantidade (kg): "+str(kg_file_duplo))
    elif kg_alcatra > 0:
        print("Tipo de carne: Alcatra")
        print("Quantidade (kg): "+str(kg_alcatra))
    else:
        print("Tipo de carne: Picanha")
        print("Quantidade (kg): "+str(kg_picanha))

    print("Total: R$"+str(total))

    if cartao_tabajara == "Sim":
        desconto = (5/100 * total)
        total = total - desconto
        print("Desconto: R$"+str(desconto))

    print("Total a pagar: R$"+str(total))