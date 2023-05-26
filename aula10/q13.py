def desenha(linhas, colunas):
    for linha in range(linhas):
        if linha == 0 or linha == (linhas - 1):
            print("+", end="")
        else:
            print("|", end="")
        for coluna in range(colunas - 2):
            if linha == 0 or linha == (linhas - 1):
                print("-", end="")
            else:
                print(" ", end="")
        if linha == 0 or linha == (linhas - 1):
            print("+", end="")
        else:
            print("|", end="")
        print("")
            
n_linhas = input("Digite o número de linhas: ")
n_linhas = int(n_linhas)
n_colunas = input("Digite o número de colunas: ")
n_colunas = int(n_colunas)
desenha(n_linhas, n_colunas)