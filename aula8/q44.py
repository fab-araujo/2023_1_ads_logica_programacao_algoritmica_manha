final = input("Digite o valor de n: ")
final = int(final)

n = 1
m = 1

soma = 0

while n <= final:
    print(str(n)+"/"+str(m))
    soma = soma + (n/m)
    n = n + 1
    m = m + 2

print(soma)