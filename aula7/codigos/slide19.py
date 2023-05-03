nota = input("Digite uma nota: ")
nota = float(nota)

while nota < 0 or nota > 10:
    print("Notá inválida!")
    nota = input("Digite uma nota: ")
    nota = float(nota)

print("Obrigado!")

