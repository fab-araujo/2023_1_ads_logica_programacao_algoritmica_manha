"""
14.	João Papo-de-Pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
peso = input("Seu João, digite o peso dos peixes: ")
peso = float(peso)
excesso = peso - 50
multa = excesso * 4

peso = str(peso)
excesso = str(excesso)
multa = str(multa)

print("O peso de peixes é: "+peso)
print("O excesso foi: "+excesso)
print("A multa é: R$"+multa)
