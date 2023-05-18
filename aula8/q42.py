nome = "Teste"

while nome != "":
    nome = input("Digite o nome do atleta: ")
    if nome != "":
        saltos = []
        melhor_salto = 0
        pior_salto = 10000
        soma = 0
        for i in range (7):
            salto = input("Digite o valor do salto: ")
            salto = float(salto)
            saltos.append(salto)
            soma = soma + salto
            if salto > melhor_salto:
                melhor_salto = salto
            if salto < pior_salto:
                pior_salto = salto
                
        print("Atleta: "+nome)
        print("Nota: "+str(saltos[0]))
        print("Nota: "+str(saltos[1]))
        print("Nota: "+str(saltos[2]))
        print("Nota: "+str(saltos[3]))
        print("Nota: "+str(saltos[4]))
        print("Nota: "+str(saltos[5]))
        print("Nota: "+str(saltos[6]))

        print("Resultado final:")
        print("Atleta: "+nome)

        print("Melhor nota: "+str(melhor_salto))
        print("Pior nota: "+str(pior_salto))
        soma = soma - melhor_salto - pior_salto
        media = soma / 5
        print("Média:"+str(media))
        
        