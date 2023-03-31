turno = input("Qual turno você estuda? Digite M para Matutino, V para Vespertino ou N para Norturno: ")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Você digitou uma opção inválida!")