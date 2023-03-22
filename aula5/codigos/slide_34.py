peso = input("Seu João, digite o peso dos peixes: ")
peso = float(peso)
if peso < 50:
    print("Você não precisa pagar multa!")
else:
    excesso = peso - 50
    multa = excesso * 4

    peso = str(peso)
    excesso = str(excesso)
    multa = str(multa)

    print("O peso de peixes é: "+peso)
    print("O excesso foi: "+excesso)
    print("A multa é: R$"+multa)
