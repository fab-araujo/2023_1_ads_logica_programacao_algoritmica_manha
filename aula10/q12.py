import random
def embaralha(palavra):
    randomlist = random.sample(range(len(palavra)), len(palavra))
    for index in randomlist:
        print(palavra[index],end="")
    print("")

palavra = input("Digite uma palavra: ")
embaralha(palavra)