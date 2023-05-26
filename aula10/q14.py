import itertools

def quadradoMagico():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    combinacoes = itertools.permutations(numeros)
    for ln in list(combinacoes):
        if  (ln[0] + ln[1] + ln[2]) == (ln[3] + ln[4] + ln[5]) == \
            (ln[6] + ln[7] + ln[8]) == (ln[0] + ln[3] + ln[6]) == \
            (ln[1] + ln[4] + ln[7]) == (ln[2] + ln[5] + ln[8]) == \
            (ln[0] + ln[4] + ln[8]) == (ln[2] + ln[4] + ln[6]):
            print("=====")
            print(str(ln[0]) + " " + str(ln[1]) + " " + str(ln[2]))
            print(str(ln[3]) + " " + str(ln[4]) + " " + str(ln[5]))
            print(str(ln[6]) + " " + str(ln[7]) + " " + str(ln[8]))
            print("=====")

quadradoMagico()