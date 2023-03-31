numero = input("Digite um número menor que 1000: ")
numero = int(numero)

if numero >= 1000:
    print("Você digitou um número inválido")
else:
    centenas = numero // 100
    dezenas = (numero - (100 * centenas)) // 10
    unidades = (numero - (100 * centenas) - (10 * dezenas))

    saida = ""

    if centenas > 0:
        saida = saida + str(centenas)
        if centenas > 1:
            saida = saida + ' centenas'
        else:
            saida = saida + ' centena'
    
    if dezenas > 0:
        if centenas != 0 and unidades == 0:
            saida = saida + ' e '
        elif centenas != 0:
            saida = saida + ', '
        saida = saida + str(dezenas)
        if dezenas > 1:
            saida = saida + ' dezenas'
        else:
            saida = saida + ' dezena'

    if unidades > 0:
        if centenas != 0 or dezenas != 0:
            saida = saida + ' e '
        saida = saida + str(unidades)
        if unidades > 1:
            saida = saida + ' unidades'
        else:
            saida = saida + ' unidade'

    print(saida)