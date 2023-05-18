cds = input("Digite o total de cds: ")
cds = int(cds)

total_gasto = 0

for i in range(cds):
    gasto = input("Digite o valor do cd: ")
    gasto = int(gasto)
   
    total_gasto = total_gasto + gasto

print(total_gasto/cds)