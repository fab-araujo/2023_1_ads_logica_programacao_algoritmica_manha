respostas_positivas = 0

q1 = input("Telefonou para a vítima? Sim ou Não: ")
if q1 == "Sim":
    respostas_positivas = respostas_positivas + 1

q2 = input("Esteve no local do crime? Sim ou Não: ")
if q2 == "Sim":
    respostas_positivas = respostas_positivas + 1  

q3 = input("Mora perto da vítima? Sim ou Não: ")
if q3 == "Sim":
    respostas_positivas = respostas_positivas + 1  

q4 = input("Devia para a vítima? Sim ou Não: ")
if q4 == "Sim":
    respostas_positivas = respostas_positivas + 1  

q5 = input("Já trabalhou com a vítima? Sim ou Não: ")
if q5 == "Sim":
    respostas_positivas = respostas_positivas + 1  

if respostas_positivas == 2:
    print("Suspeito")
elif respostas_positivas == 3 or respostas_positivas == 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")