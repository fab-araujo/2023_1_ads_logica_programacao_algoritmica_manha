num1 = input("Digite o primeiro número: ")
num1 = float(num1)

num2 = input("Digite o segundo número: ")
num2 = float(num2)

num3 = input("Digite o terceiro número: ")
num3 = float(num3)

if num1 > num2 and num1 > num3:
    print(str(num1) + " é o maior número")
elif num2 > num1 and num2 > num3:
    print(str(num2) + " é o maior número")
else:
    print(str(num3) + " é o maior número")