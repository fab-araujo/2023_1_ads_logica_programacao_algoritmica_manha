num1 = input("Digite o primeiro número: ")
num1 = float(num1)

num2 = input("Digite o segundo número: ")
num2 = float(num2)

num3 = input("Digite o terceiro número: ")
num3 = float(num3)

if (num1 > num2) and (num1 > num3):
    print(num1)
    if (num2 > num3):
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 > num1 and num2 > num3:
    print(num2)
    if (num1 > num3):
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if (num1 > num2):
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)