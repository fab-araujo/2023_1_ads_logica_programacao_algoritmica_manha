n = input("Quantas pessoas vão participar? ")
n = int(n)
soma = 0

for i in range(n):
    idade = input("Digite uma idade: ")
    idade = float(idade)
    soma = soma + idade

media = (soma/n)

print(media)
if media <= 25:
    print("Jovem")
elif media > 25 and media <= 60:
    print("Adulta")
else: 
    print("Idosa")