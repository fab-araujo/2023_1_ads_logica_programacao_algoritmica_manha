def reversoN(n):
    n = str(n)
    fim = len(n) - 1
    while fim >= 0:
        print(n[fim], end="")
        fim = fim - 1
    print("")

reversoN(721)