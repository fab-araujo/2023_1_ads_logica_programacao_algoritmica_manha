#slide39
nome_cachorro = input("Digite o nome do seu cachorro: ")
idade_cachorro = input("Digite a idade do seu cachorro: ")
int_idade_cachorro = int(idade_cachorro)
idade_cachorro_humano = int_idade_cachorro * 7
str_cachorro_humano = str(idade_cachorro_humano)
print("O "+nome_cachorro+" tem "+str_cachorro_humano+" em anos humanos")