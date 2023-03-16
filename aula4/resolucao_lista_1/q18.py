"""
18.	Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tamanho = input("Digite o tamanho do arquivo para download: ")
tamanho = float(tamanho)
velocidade = input("Digite a velocidade do link: ")
velocidade = float(velocidade)
tempo_segundos = tamanho / velocidade
tempo_minutos = tempo_segundos / 60
tempo_minutos = round(tempo_minutos,2)
print(tempo_minutos)