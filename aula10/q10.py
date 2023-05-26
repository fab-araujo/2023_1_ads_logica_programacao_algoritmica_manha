def craps(num_jogada, dado, ponto):
    if num_jogada == 1 and (dado == 7 or dado == 11):
        return "Natural"
    elif num_jogada == 1 and (dado == 2 or dado == 3 or dado == 12):
        return "Craps"
    elif num_jogada == 1:
        return "Ponto"
    elif dado == 7:
        return "Perdeu o ponto"
    elif dado == ponto:
        return "Ganhou o ponto"
    return ""
    
dado = input("Digite o valor dos dados: ")
dado = int(dado)
jogada = 1

resultado = craps(jogada, dado, 0)
print(resultado)
if resultado == "Ponto":
    ponto = dado
    resultado = ""
    while resultado == "":
        dado = input("Digite o valor dos dados: ")
        dado = int(dado)
        jogada = jogada + 1
        resultado = craps(jogada, dado, ponto)
    print(resultado)