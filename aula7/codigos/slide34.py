bits = []
n_bits = 8
contador = 0

while contador < n_bits:
    bit = input("Digite um bit: ")
    bit = int(bit)
    bits.append(bit)
    contador = contador + 1

index = 0
n0s = 0
n1s = 0
while index < n_bits:
    if bits[index] == 0:
        n0s = n0s + 1
    else:
        n1s = n1s + 1

    index = index + 1

print(n0s)
print(n1s)


