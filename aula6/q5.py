produto1 = input("Digite o valor do primeiro produto: ")
produto1 = float(produto1)

produto2 = input("Digite o valor do segundo produto: ")
produto2 = float(produto2)

produto3 = input("Digite o valor do terceiro produto: ")
produto3 = float(produto3)

if produto1 < produto2 and produto1 < produto3:
    print("Você deve comprar o primeiro produto")
elif produto2 < produto1 and produto2 < produto3:
    print("Você deve comprar o segundo produto")
else:
    print("Você deve comprar o terceiro produto")