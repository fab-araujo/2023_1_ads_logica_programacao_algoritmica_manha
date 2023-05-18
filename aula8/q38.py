n_cq = 0
n_bs = 0
n_bo = 0
n_h = 0
n_c = 0
n_r = 0
total = 0
codigo = 1

while codigo != 0:
    codigo = input("Digite o código: ")
    codigo = int(codigo)
    if codigo != 0:
        quantidade = input("Digite a quantidade: ")
        quantidade = int(quantidade)

        if codigo == 100:
            n_cq = n_cq + quantidade
            total = total + (quantidade * 1.2)
        elif codigo == 101:
            n_bs = n_bs + quantidade
            total = total + (quantidade * 1.3)
        elif codigo == 102:
            n_bo = n_bo + quantidade
            total = total + (quantidade * 1.5)
        elif codigo == 103:
            n_h = n_h + quantidade
            total = total + (quantidade * 1.2)
        elif codigo == 104:
            n_c = n_c + quantidade
            total = total + (quantidade * 1.3)
        elif codigo == 105:
            n_r = n_r + quantidade
            total = total + (quantidade * 1)

print("Cachorro Quente: R$ 1,20 x "+str(n_cq)+" = R$ "+str(n_cq * 1.2))
print("Bauru Simples: R$ 1,30 x "+str(n_bs)+" = R$ "+str(n_bs * 1.3))
print("Bauru com ovo: R$ 1,50 x "+str(n_bo)+" = R$ "+str(n_bo * 1.5))
print("Hambúrguer: R$ 1,20 x "+str(n_h)+" = R$ "+str(n_h * 1.2))
print("Cheeseburguer: R$ 1,30 x "+str(n_c)+" = R$ "+str(n_c * 1.3))
print("Refrigerante: R$ 1,00 x "+str(n_r)+" = R$ "+str(n_r * 1.0))
print(total)