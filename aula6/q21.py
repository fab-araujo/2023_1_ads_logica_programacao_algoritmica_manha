num1 = input("Digite um número: ")
num1 = float(num1)

num2 = input("Digite outro número: ")
num2 = float(num2)

opr = input("Digite a operação, sendo '+' para soma, '-', para subtração, '*' para multiplicação e '/' para divisão: ")
if opr == "+" or opr == "-" or opr == "*" or opr == "/":
    if opr == "+":
        resultado = num1 + num2
    elif opr == "-":
        resultado = num1 - num2
    elif opr == "*":
        resultado = num1 * num2
    elif opr == "/":
        resultado = num1 / num2

    print("O resultado entre "+str(num1)+opr+str(num2)+" é: "+str(resultado))
    if resultado % 2 == 0:
        print(str(resultado)+" é par")
    else:
        print(str(resultado)+" é impar")

    if resultado > 0:
        print(str(resultado)+" é positivo")
    else:
        print(str(resultado)+" é negativo")

    parte_inteira = int(resultado)
    parte_decimal = resultado - parte_inteira

    if parte_decimal > 0:
        print(str(resultado) + " é decimal")
    else:
        print(str(int(resultado)) + " é inteiro")
else:
    print("Operação inválida!")