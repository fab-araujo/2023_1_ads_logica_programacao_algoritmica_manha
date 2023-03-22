media = input("Qual foi a sua média no semestre? ")
media = float(media)
if media < 4:
    print("Você está reprovado")
elif media >= 4 and media < 7:
    print("Você deve fazer a prova final")
else:
    print("Você foi aprovado direto")