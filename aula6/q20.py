num = input("Digite um número: ")
num = float(num)

parte_inteira = int(num)
parte_decimal = num - parte_inteira

if parte_decimal > 0:
    print(str(num) + " é decimal")
else:
    print(str(int(num)) + " é inteiro")