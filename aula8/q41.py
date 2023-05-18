nome = "Teste"

while nome != "":
    nome = input("Digite o nome do atleta: ")
    if nome != "":
        saltos = []
        melhor_salto = 0
        pior_salto = 10000
        soma = 0
        for i in range (5):
            salto = input("Digite o valor do salto: ")
            salto = float(salto)
            saltos.append(salto)
            soma = soma + salto
            if salto > melhor_salto:
                melhor_salto = salto
            if salto < pior_salto:
                pior_salto = salto
                
        print("Atleta: "+nome)
        print("Primeiro salto: "+str(saltos[0]))
        print("Segundo salto: "+str(saltos[1]))
        print("Terceiro salto: "+str(saltos[2]))
        print("Quarto salto: "+str(saltos[3]))
        print("Quinto salto: "+str(saltos[4]))
        print("Melhor salto: "+str(melhor_salto))
        print("Pior salto: "+str(pior_salto))
        soma = soma - melhor_salto - pior_salto
        media = soma / 3
        print("Média dos demais saltos:"+str(media))
        print("Resultado final:")
        print(nome+": "+str(media))