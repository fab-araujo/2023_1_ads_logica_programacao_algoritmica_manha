gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

opcao = "Sim"

maior_nota = 0
menor_nota = 10
soma = 0
contador = 0

while opcao == "Sim":
    nota = 0
    for i in range(10):
        letra = input("Digite a sua letra: ")
        if letra == gabarito[i]:
            nota = nota + 1

    if nota > maior_nota:
        maior_nota = nota

    if nota < menor_nota:
        menor_nota = nota

    soma = soma + nota
    contador = contador + 1

    opcao = input("Deseja continuar? ")

print(maior_nota)
print(menor_nota)
print(contador)
print(soma/contador)
    
