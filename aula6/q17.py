nota1 = input("Digite a sua primeira nota: ")
nota1 = float(nota1)

nota2 = input("Digite a sua segunda nota: ")
nota2 = float(nota2)

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

print(media)