nota1 = input("Digite a sua primeira nota: ")
nota1 = float(nota1)

nota2 = input("Digite a sua segunda nota: ")
nota2 = float(nota2)

media = (nota1 + nota2) / 2

print("Sua nota na primeira avaliação foi: "+str(nota1))
print("Sua nota na segunda avaliação foi: "+str(nota2))
print("Sua média nas avaliações foi: "+str(media))

if media >= 9 and media <= 10:
    print("Aprovado")
elif media >= 7.5 and media < 9:
    print("Aprovado")
elif media >= 6 and media < 7.5:
    print("Aprovado")
elif media >= 4 and media < 6:
    print("Reprovado")
else:
    print("Aprovado")