votos_A = 0
votos_B = 0
votos_C = 0
votos_D = 0
nulos = 0
branco = 0

opcao = input("Digite a sua opção: ")
opcao = int(opcao)

while opcao != 0:
    if opcao == 1:
        votos_A = votos_A + 1
    elif opcao == 2:
        votos_B = votos_B + 1
    elif opcao == 3:
        votos_C = votos_C + 1
    elif opcao == 4:
        votos_D = votos_D + 1
    elif opcao == 5:
        nulos = nulos + 1
    elif opcao == 6:
        branco = branco + 1
    
    opcao = input("Digite a sua opção: ")
    opcao = int(opcao)

print(votos_A)
print(votos_B)
print(votos_C)
print(votos_C)
print(nulos)
print(branco)

total = votos_A + votos_B + votos_C + votos_D

print(nulos * 100 / total)
print(branco * 100 / total)
