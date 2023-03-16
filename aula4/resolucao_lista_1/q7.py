"""
7.	Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
lado = input("Digite o valor dos lados do quadrado: ")
lado = int(lado)
area = lado ** 2
print(area)
area_dobrada = 2 * area
print(area_dobrada)