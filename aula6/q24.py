kg_morango = input("Quantos kilos de morango você vai comprar? ")
kg_morango = int(kg_morango)

kg_maca = input("Quantos kilos de maçã você vai comprar? ")
kg_maca = int(kg_maca)

total = 0

if kg_morango < 5:
    total = total + (kg_morango * 2.5)
else:
    total = total + (kg_morango * 2.2)

if kg_maca < 5:
    total = total + (kg_maca * 1.8)
else:
    total = total + (kg_maca * 1.5)

if (kg_maca + kg_morango) >= 8 or total >= 25:
    total = total - (10/100 * total)

print(total)