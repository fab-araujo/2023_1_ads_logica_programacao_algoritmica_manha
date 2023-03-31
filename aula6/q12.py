lado1 = input("Digite o primeiro lado do triângulo: ")
lado1 = int(lado1)

lado2 = input("Digite o segundo lado do triângulo: ")
lado2 = int(lado2)

lado3 = input("Digite o terceiro lado do triângulo: ")
lado3 = int(lado3)

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os valores informados não formam um triângulo")