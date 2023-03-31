valor = input("Digite o valor do saque: ")
valor = int(valor)

if valor < 10 or valor > 600:
    print("Valor inválido!")
else:
    n_100 = valor // 100
    n_50 = (valor - (n_100 * 100)) // 50
    n_10 = (valor - (n_100 * 100) - (n_50 * 50)) // 10
    n_5 = (valor - (n_100 * 100) - (n_50 * 50) - (n_10 * 10)) // 5
    n_1 = (valor - (n_100 * 100) - (n_50 * 50) - (n_10 * 10) - (n_5 * 5))

    print("Seu saque será em: ")

    if n_100 > 0:
        print(str(n_100)+" nota(s) de 100")

    if n_50 > 0:
        print(str(n_50)+" nota(s) de 50")

    if n_10 > 0:
        print(str(n_10)+" nota(s) de 10")

    if n_5 > 0:
        print(str(n_5)+" nota(s) de 5")

    if n_1 > 0:
        print(str(n_1)+" nota(s) de 1")