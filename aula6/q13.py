a = input("Informe o valor de a: ")
a = int(a)

if a == 0:
    print("A equação não é do segundo grau. Encerrando...")
else:
    b = input("Informe o valor de b: ")
    b = int(b)

    c = input("Informe o valor de c: ")
    c = int(c)

    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        print("A equação não possui raizes reais.")
    elif delta == 0:
        x = (-b) / (2 * a)
        print(x)
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print(x1)
        print(x2)