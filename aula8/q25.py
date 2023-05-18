total = 0

valor = input("Digite o valor do pão: ")
valor = float(valor)

for i in range(50):
    total = total + valor
    print(str(i + 1) + " - R$ "+str(total))